import os
import time

#form an absolute path to the file

ls = os.listdir()


def iterate(ls):
    path = "C:\\Users\\sanjeev\\GitHub\\Python Projects\\Python\\find_txt_files\\files"
    
    for i in ls:
        fname = i
        fullPath = os.path.join(path, fname)
        modification_time = os.path.getmtime(fullPath)
        #local_time = time.ctime(modification_time)
        ext = i.split(".")
        b = ext[1]
        if b == "txt":
            print("File "+i+ " was modified at ")
            print(str(modification_time) +"\n")

iterate(ls)
    


