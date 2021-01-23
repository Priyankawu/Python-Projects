import os
import time

#form an absolute path to the file




def iterate():
    path = "C:\\A"
    ls = os.listdir(path)
    print(ls)
    #path = "C:\\Users\\sanjeev\\GitHub\\Python Projects\\Python\\find_txt_files\\files"
    
    for i in ls:
        fname = i
        #fullPath = os.path.join(path, fname)
        modification_time = os.path.getmtime(path)
        #local_time = time.ctime(modification_time)
        ext = i.split(".")
        b = ext[1]
        if b == "txt":
            print("File "+i+ " was modified at ")
            print(str(modification_time) +"\n")

iterate()
    


