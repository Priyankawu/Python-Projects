import tkinter as tk
from tkinter import * #w/o this, sticky does not work
import webpage_main
import webpage_func


def load_gui(self):

    self.entry_box = tk.Entry(self.master,text="", bg="light gray")
    #? row, column, sticky are not in right place in gui
    self.entry_box.grid(row=0, column=0)

    self.bt = tk.Button(self.master,text="Create", width=15,
                height=2,command=lambda:webpage_func.createHTML_file(self.entry_box.get()))
    self.bt.grid(row=1, column=0)

   



if __name__=="__main__":
    pass
