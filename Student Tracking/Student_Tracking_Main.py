# Python Version: 3.11.3
#
# Autho: Bret Morris

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# import other modules to have access
import Student_Tracking_GUI
import Student_Tracking_Func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        # Using CenterWindow will center the app on the screen
        Student_Tracking_Func.center_window(self,500,300)
        self.master.title("Student Tracking Demo")
        self.master.configure(bg="#F0F0F0")
        # Using this protocol method allows to catch if the user
        # clicks on the 'X' in the upper corner
        self.master.protocol("WM_DELETE_WINDOW", lambda: Student_Tracking_Func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module
        Student_Tracking_GUI.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=1,accelerator='Ctrl+Q',command=lambda: Student_Tracking_Func.ask_quit(self))
        menubar.add_cascade(label='FIle', underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label='How to use this program')
        helpmenu.add_separator()
        helpmenu.add_command(label='About This Student Tracking Demo')
        menubar.add_cascade(label='Help', menu=helpmenu)
        self.master.config(menu=menubar, borderwidth='1')




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



    
    
