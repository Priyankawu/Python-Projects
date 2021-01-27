from tkinter import *
import tkinter as tk
import sqlite3
import os

import tracking_main
import tracking_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):#title and message arguments
        self.master.destroy()
        os._exit(0)

############################## CREATING THE DATABASE #####################################
#sql statements end in a semi-colon
def create_db(self):
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT, \
        col_lname TEXT, \
        col_fullname TEXT, \
        col_phone TEXT, \
        col_email TEXT, \
        col_course TEXT)")
        conn.commit()
    conn.close()
    first_run(self) #fill one entry automatically so it doesn't give any errors
    
def first_run(self):
    data = ("Priyanka","Thakan",'Priyanka Thakan','888-888-8888','priyanka@earth.com','Coding Bootcamp')
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur,count=count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO tbl_students(col_fname,col_lname,col_fullname,col_phone,col_email,col_course) \
            VALUES (?,?,?,?,?,?)",data);
            conn.commit()
    conn.close()

def count_records(cur):
    count=""
    cur.execute("SELECT COUNT(*) from tbl_students")
    count = cur.fetchone()[0]
    return cur,count
########################### CREATED DATABASE WITH ONE ENTRY IN THE BEGINNING #############################

#Delete the item the user selects to delete
def onSelect(self,event):
    varList = event.widget
    
    select = varList.curselection()[0] #comes as tuple
    print(select)
    value = varList.get(select)#fullname
    print(value)

    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute(""" SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students
    WHERE col_fullname =(?),"""[value])
    varBody = cursor.fetchall() #return a tuple
    conn.commit()   # I put these two lines
    conn.close()    #
    varBody = cursor.fetchall() #return a tuple
    #slice the varBody tuple
    for data in varBody:
        self.txt_fname.delete(0,END)#delete from 0 to last
        self.txt_fname.insert(0,data[0])
        self.txt_lname.delete(0,END)
        self.txt_lname.insert(0,data[1])
        self.txt_phone.delete(0,END)
        self.txt_phone.insert(0,data[2])
        self.txt_email.delete(0,END)
        self.txt_email.insert(0,data[3])
        self.txt_course.delete(0,END)
        self.txt_course.insert(0,data[4])

############################### ADDING TO LIST WHEN SUBMIT BUTTON IS PRESSED ########################
def addToList(self):
    var_fname = self.txt_fname.get()    # get(): gets the text from the entry boxes
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip()         #remove blank spaces before and after
    var_lname = var_lname.strip()
    var_fname = var_fname.title()       # capitalizes the first letter
    var_lname = var_lname.title()
    var_fullname = ("{},{}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()

    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and(len(var_email)>0) and(len(var_course)>0):
        conn = sqlite3.connect('db_students.db')
        with conn:
            cur = conn.cursor()
            cur.execute(""" SELECT COUNT(col_fullname) FROM tbl_students \
                    WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0: #no fullname in db so we can add data
                print("chkName: {}".format(chkName))
                cur.execute("""INSERT INTO tbl_students(col_fname,col_lname,col_fullname,col_phone,col_email,col_course) \
                VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.listBox1.insert(END,var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists in the databse! Please choose a different name.".format(var_fullname))
                onClear(self) #call the function to clear all teh textboxes
            conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")

def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_course.delete(0,END)

def onDelete(self):
    var_select = self.listBox1.get(self.listBox1.curselection()) #selected value in listBox
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*)FROM tbl_students")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All informaiton associated with, ({}) \n \
                    will be permanently deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_students.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM tbl_students WHERE col_fullname='{}':".format(var_select))
                onDeleted(self)
                onRefresh(self)
            conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in teh database and canno tbe deleted at this time. \
                                \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()
    
def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_course.delete(0,END)
    try:
        index = self.listBox1.curselection()[0]
        self.listBox.delete(index)
    except IndexError:
        pass

def onRefresh(self):
    #Populate the lsitbox, coinciding with the database
    self.listBox1.delete(0,END)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        i=0
        while i<count:
            cur.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.listBox1.insert(0,str(item))
                i+=1
    conn.close();
    
    

if __name__ == "__main__":
    pass
