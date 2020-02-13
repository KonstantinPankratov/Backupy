from Backupy import Backupy
import os


def test_backup_directory():
    backup = Backupy()
    backup2 = Backupy(save_to='/var/')

    assert backup.destination == os.getcwd()
    assert backup2.destination == '/var/'
