#This is to work with the os and shutil (file operations for one or multiple files)
# module to transfer/copy/delete files in your python program

import os
import shutil
import time

def file_transfer():
    #set where the source of files are- FolderA
    """ Notice the '/' everywhere and even in the end """

    source= "C:/Users/sanjeev/Desktop/FolderA/"
    # set where the destination of files is- FolderB
    destination= "C:/Users/sanjeev/Desktop/FolderB/"
    files = os.listdir(source)
    current_time = time.time()
    print(current_time)

    #atime:last accesstime, mtime: last modificationtime, ctime: last changetime
    # move all the files in source to destination
    for i in files:
        #modification epoch time
        mtime = os.stat(source+i).st_mtime
        print("Modification time: {}".format(mtime))
        #find difference in current_time and mtime to see file was modified within
        # the last 10 hours= 86400sec
        diff = current_time-mtime
        print("Difference is: {}".format(diff))
        if(diff < 86400): #last 24 hours=86400sec
            shutil.move(source+i,destination)
     


