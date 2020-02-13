from Backupy import Backupy

backup = Backupy()
backup.add_directory(
    backup_directory='/var/www/html/assets/',
    exclude_directories={
        'images',
        'fonts'
    }
)
backup.start()
