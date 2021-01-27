
import tkinter as tk
from tkinter import filedialog
import pytz

import ch_main
import ch_gui





def text_path(self):
    path = filedialog.askdirectory() #path a stringVar
    self.txt1.insert(0,path)
    
    
    
    #when button is pressed, user's selected path is retained by
    #askdirectory() method and printed in GUI's text widget
    
