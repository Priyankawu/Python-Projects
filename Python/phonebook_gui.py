from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have acces to them
import phonebook_main
import phonebook_func


def load_gui(self):

    self.lbl_fname = tk.Label(self.master, text="First Name")
    self.lbl_fname.grid(row=0, column=0 padx=(27,0), pady=(10,0),sticky=N+W)

    self.lbl_lname = tk.Label(self.master, text="First Name")
    self.lbl_lname.grid(row=1, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.lbl_phone = tl.Label(self.master, text="Phone Number")
    self.lbl_phone.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.lbl_email = t1.Label(self.master, text="Email")
    self.lbl_email.grid(row=3, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.lbl_user = t1.Label(self.master, text="User")
    self.lbl_user.grid(row=0, column=1, padx=(0,0), pady=(10,0), sticky=N+W)
    








def load_gui():
    
