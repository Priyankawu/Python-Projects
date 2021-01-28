import tkinter as tk
from tkinter import * #w/o this, sticky does not work
import webpage_main
import webpage_func

#This function makes the entry box and the create button that creates the html file
# and opens it in the browser.
def load_gui(self):

    self.entry_box = tk.Entry(self.master,text="", bg="light gray", width = 45)

    self.entry_box.grid(row=0, column=0, padx=(10,10), pady=(30,20))

    self.bt = tk.Button(self.master,text="Create", width=15,
                height=2,command=lambda:webpage_func.createHTML_file(self.entry_box.get()))
    self.bt.grid(row=1, padx=(10,10),column=0)

   



if __name__=="__main__":
    pass
