from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tracking_gui
import tracking_func


#?What is the master?
#creates the main window, then tracking_gui adds the widgets
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs) #Need more parameters here
        self.master = master
        self.master.maxsize(500,400)
        self.master.minsize(500,400)
        self.master.title("Student Tracking System Application")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracking_func.ask_quit(self))
        #load gui widgets from tracking_gui
        tracking_gui.load_gui(self)
        








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)    #this only shows the window once
    root.mainloop()             #loop to keep having the window on screen
    
