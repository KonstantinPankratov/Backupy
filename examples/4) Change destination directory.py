from Backupy import Backupy

"""
save_to contains a path to the directory where backups will be saved
By default, it is current working directory
"""

backup = Backupy(save_to='/home/backup/')
backup.add_directory('/var/www/html/assets/')
backup.start()
