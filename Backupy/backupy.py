import os
import zipfile
from datetime import datetime


class Backupy:
    destination = os.getcwd()
    backup = list()
    exclude = list()
    compress = True

    filename = None
    filename_prefix = 'backup_'
    filename_format = '{prefix}{date}'
    date_format = '%d-%m-%Y'

    def add_directory(self, directory):
        self.backup.append(directory)
        return self.backup

    def start(self):
        self.set_filename()

        if self.compress:
            zipf = zipfile.ZipFile(os.path.join(self.destination, self.filename), 'w', zipfile.ZIP_DEFLATED)
            for d in self.backup:
                self.__zip(d, zipf)
                zipf.close()

    def set_destination(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except PermissionError:
                raise
            except OSError:
                if not os.path.isdir(path):
                    raise
        self.destination = path
        return self.destination

    def set_filename(self):
        date = datetime.today().strftime(self.date_format)
        self.filename = self.filename_format.format(prefix=self.filename_prefix, date=date)
        return self.filename

    def set_filename_prefix(self, prefix):
        self.filename_prefix = prefix
        return self.filename_prefix

    def set_date_format(self, format):
        try:
            datetime.today().strftime(format)
            self.date_format = format
        except ValueError:
            raise ValueError("Incorrect date format.")
        return self.date_format

    @staticmethod
    def __zip(path, zipf):
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))

