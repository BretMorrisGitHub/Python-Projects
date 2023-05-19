import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # creates the GUI title
        self.master.title("Web Page Generator")
        # creates and positions the defaultHTML button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10) , pady=(10,10))
        # creates and positions the submitHTML button
        self.btn2 = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.submitHTML)
        self.btn2.grid(row=2, column=1, padx=(10,10) , pady=(10,10))
        # creates and positions the custom text input box and label
        self.customInput = Entry(self.master, width = 75)
        self.customInput.grid(row=1, column=0, columnspan=2, padx=(20,10), pady=(30,0))
        self.customInputLabel = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.customInputLabel.grid(row=0,column=0)


    # creates a function to submit default text
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    # creates a function to submit custom input 
    def submitHTML(self):
        htmlText = self.customInput.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
