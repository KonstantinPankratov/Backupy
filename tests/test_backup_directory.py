from Backupy import Backupy


def test_backup_directory():
    backup = Backupy()
    assert backup.backup == list()

    backup.add_directory('/test/')
    assert backup.backup == ['/test/']