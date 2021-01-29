
import tkinter as tk
from tkinter import filedialog
import pytz

import ch_main
import ch_gui

import os
import shutil
import time


def text_path1(self):
    path = filedialog.askdirectory() #path a stringVar?
    self.txt1.insert(0,path)

def text_path2(self):
    path = filedialog.askdirectory() #path a stringVar?
    self.txt2.insert(0,path)
    #when button is pressed, user's selected path is retained by
    #askdirectory() method and printed in GUI's text widget
    

#Transfers the files feom the source to the destination folder
def file_transfer(self):
  
    """ Notice the '/' everywhere and even in the end """
    # Get the source path from the Entry box
    source= self.txt1.get()#"C:/Users/sanjeev/Desktop/FolderA/"
    source = source + '/'
    #print(source)
    # get the destination path from the Entry box
    destination= self.txt2.get() + "/"#"C:/Users/sanjeev/Desktop/FolderB/"
    files = os.listdir(source)
    current_time = time.time()
    #print(current_time)

    #atime:last accesstime, mtime: last modificationtime, ctime: last changetime
    # move all the files in source to destination
    for i in files:
        #modification epoch time
        mtime = os.stat(source+i).st_mtime
        #print("Modification time: {}".format(mtime))
        #find difference in current_time and mtime to see file was modified within
        # the last 10 hours= 86400sec
        diff = current_time-mtime
        #print("Difference is: {}".format(diff))
        if(diff < 86400): #last 24 hours=86400sec
            shutil.move(source+i,destination)
     
