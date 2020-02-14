import os
import zipfile
from datetime import datetime
from fnmatch import fnmatch


class Backupy:
    dirs = list()
    exclude = dict()
    backup_dir = None

    filename = None
    filename_prefix = None
    filename_format = None
    date_format = None

    def __init__(self, backup_directory=os.getcwd(), filename_prefix='backup_', filename_format='{prefix}{date}', date_format='%d-%m-%Y'):
        self.filename_prefix = filename_prefix
        self.filename_format = filename_format
        self.date_format = date_format
        self.__set_backup_dir(backup_directory)
        self.__set_filename()

    def add_directory(self, directory, exclude=None):
        self.exclude[directory] = list()

        if exclude:
            for d in exclude:
                self.exclude[directory].append(d)

        self.dirs.append(directory)
        return self.dirs

    def start(self):
        if not self.dirs:
            raise Exception("No directories to backup. Use add_directory()")

        zipf = zipfile.ZipFile(os.path.join(self.backup_dir, self.filename), 'w', zipfile.ZIP_DEFLATED)
        for d in self.dirs:
            self.__zip(d, zipf)
        zipf.close()

    def __set_backup_dir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except PermissionError:
                raise
            except OSError:
                if not os.path.isdir(path):
                    raise
        self.backup_dir = path
        return self.backup_dir

    def __set_filename(self):
        date = datetime.today().strftime(self.date_format)
        self.filename = self.filename_format.format(prefix=self.filename_prefix, date=date)
        return self.filename

    def __zip(self, path, zipf):
        for root, dirs, files in os.walk(path):
            parent = os.path.relpath(root, path)
            if path in self.exclude and len(self.exclude[path]) != 0:
                for d in dirs:
                    for ex in self.exclude[path]:
                        if ex.startswith('/'):
                            ex = ex[1:]
                        if os.path.normpath(os.path.join(parent, d)) == ex:
                            dirs.remove(d)
            for file in files:
                skip = False
                complete = os.path.join(root, file)
                if path in self.exclude and len(self.exclude[path]) != 0:
                    for ex in self.exclude[path]:
                        if ex.startswith('/'):
                            ex = ex[1:]
                        if fnmatch(complete, os.path.join(path, ex)):
                            files.remove(file)
                            skip = True
                if complete not in self.exclude and not skip:
                    zipf.write(complete)
