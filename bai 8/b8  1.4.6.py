print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

from tkinter import *
def NewFile():
 print("New File!")
def About():
 print("This is a simple example of a menu")
 
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()
