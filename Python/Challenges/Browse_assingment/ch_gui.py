#step 262: gui not like in assignment
from tkinter import *
import tkinter as tk
import ch_main
import ch_func


def load_gui(self):
    self.btn_browse1 = tk.Button(self.master,text = "Browse...", width=13, command =lambda:ch_func.text_path(self))
    self.btn_browse1.grid(row=1, column=0, padx=(20,0), pady=(50,0))
    
    self.btn_browse2 = tk.Button(self.master,text = "Browse...",width=13)
    self.btn_browse2.grid(row=2, column=0, padx=(20,0), pady=(30,0), columnspan=1)
    self.btn_check = tk.Button(self.master,text="Check for files...",width=13, height=2)
    self.btn_check.grid(row=3, column=0, padx=(20,0), pady=(30,0),sticky=S+W)
    
    self.btn_close = tk.Button(self.master, text="Close Program", height=2,width=13)
    self.btn_close.grid(row=3, column=2)
    
    self.txt1 = tk.Entry(self.master, text="", width=50)
    self.txt1.grid(row=1, column=1, padx=(20,0), pady=(50,0))
    self.txt2 = tk.Entry(self.master, text="", width=50)
    self.txt2.grid(row=2, column=1, padx=(20,0), pady=(30,0))
        
if __name__=="__main__":
    pass
