from Backupy import Backupy


def test_backup_directory():
    backup = Backupy()
    assert backup.dirs == list()

    backup.add_directory('/test/')
    assert backup.dirs == ['/test/']