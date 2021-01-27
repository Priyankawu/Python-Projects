#? Doesn't look like step 262

from tkinter import *
import tkinter as tk
import ch_gui
import ch_func

class ParentWindow(Frame):  #Frame is the Parent. Frame is the container for other widgets.
    def __init__(self, master):
        Frame.__init__(self,master)
        #define our master frame configuration
        self.master = master
        self.master.title("Check files")
        self.master.maxsize(600,250)
        self.master.minsize(600,250)

        ch_gui.load_gui(self)
        



if __name__ == "__main__":

    root = tk.Tk(); #Tk class is used to create a root window.
    app = ParentWindow(root)
    root.mainloop()
