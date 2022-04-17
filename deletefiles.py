import os
import shutil
import time

path=''
destination=''
days=30
seconds=time.time()-(days*24*60*60)
listoffiles=os.listdir(path)
for file in listoffiles:
    filetime=os.stat(file).st_ctime
    if(seconds>=filetime):
        shutil.move(file,destination)