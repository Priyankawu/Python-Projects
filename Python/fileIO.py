
import os

fName = 'Hello.txt'

fPath = 'C:\\A\\'

fullPath = (os.path.join(fPath, fName))   #joins the path and the file name
print(fullPath)
