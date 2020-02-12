from Backupy import Backupy
import os


def test_backup_directory():
    backup = Backupy()
    assert backup.destination == os.getcwd()
