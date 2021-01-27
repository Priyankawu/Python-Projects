import tkinter as tk
from tkinter import *

import webpage_gui
import webpage_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __int__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        #define our master frame configuration
        self.master = master #master of ParentWindow
        self.master.maxsize(300,500)
        self.master.minsize(300,500)

        webpage_gui.load_gui(self)






if __name__ == "__main__":
    frame = Frame()
    window = ParentWindow(frame)
    frame.mainloop()

    
    
    
