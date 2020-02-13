from Backupy import Backupy

backup = Backupy()
backup.add_directory('/var/www/html/assets/')
backup.add_directory('/etc/apache2/')
backup.start()
