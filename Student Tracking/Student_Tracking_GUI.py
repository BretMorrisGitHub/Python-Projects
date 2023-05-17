# Author: Bret Morris

from tkinter import *
import tkinter as tk

# import other modules to have access
import Student_Tracking_Func
import Student_Tracking_Main



def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phoneNum = tk.Label(self.master,text='Phone Number:')
    self.lbl_phoneNum.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,text='Current Course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phoneNum = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: Student_Tracking_Func.addToList(self))
    self.btn_submit.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: Student_Tracking_Func.onDelete(self))

    Student_Tracking_Func.create_db(self)
    Student_Tracking_Func.onRefresh(self)



if __name__ == "__main__":
    pass
