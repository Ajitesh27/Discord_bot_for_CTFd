import commands
from time import strftime
import subprocess
import os
import glob
from handlers import view_controller

view_controller.scoreboard_before_freeze()


import threading
import time
import sys



def func1():
	while True:
		time.sleep(300)
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

def func2():
        while True:
                time.sleep(300)
                view_controller.scoreboard_before_freeze()
                thetime = str(strftime("%Y-%m-%d-%H-%M")) 
                print("Scoreboard updated at ",thetime)
try:
        t1 = threading.Thread(target=func1)
        t2=threading.Thread(target=func2)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()
        commands.start()

except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
        sys.exit(1)
