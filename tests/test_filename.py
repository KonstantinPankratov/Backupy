from Backupy import Backupy
from datetime import datetime


def test_backup_directory():
    backup = Backupy()
    assert backup.set_date_format('%Y.%m.%a') == '%Y.%m.%a'

    current_date = datetime.today().strftime(backup.date_format)
    assert backup.set_filename() == 'backup_' + current_date

    backup.set_filename_prefix('backup--')
    assert backup.set_filename() == 'backup--' + current_date
