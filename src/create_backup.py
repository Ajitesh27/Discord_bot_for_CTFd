from time import strftime
import subprocess
import os
import glob
import time

def start():
 USER = "postgres"
 PASS = "postgresql"
 HOST = "localhost"
 
 BACKUP_DIR = "C:\\Users\\Prajna\\Envs\\ooadproject\\dCTF-main\\src\\Backup\\"
 dumper = dumper = """ "c:\\program files\\postgresql\\12\\bin\\pg_dump" -U %s -f %s  %s  """                 
 os.putenv('PGPASSWORD', PASS)
 database_list=["mydb"]
 for database_name in database_list :
    database_name = database_name.strip()
    glob_list = glob.glob(BACKUP_DIR + '*' + '.sql')
    for file in glob_list:
        file_info = os.stat(file)
        os.unlink(file)
 for database_name in database_list :
    thetime = str(strftime("%Y-%m-%d-%H-%M")) 
    file_name = 'Backup_'+database_name + '_' + thetime+'.sql'
    command = dumper % (USER,  BACKUP_DIR + file_name, database_name)
    subprocess.call(command,shell = True)
 print("Backup at ",thetime," complete.")
