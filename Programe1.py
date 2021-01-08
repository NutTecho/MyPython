from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import colorchooser
from tkinter import filedialog
import sys

# set interface
gui = Tk()
gui.title("Programe copy multifile")
setfont = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
#  geometry width x height
gui.geometry("800x400")
# gui.minsize(400,400)
# gui.maxsize(600,600)
gui.resizable(height = False,width = False)
# gui.option_add("*Font","consolas,10")


def testdata(e):
    # filedialog.askopenfile()
    file = filedialog.askdirectory()
    # file2 = filedialog.askopenfilename(title = "test",filetype = [('Excel')])
    # saveFile = filedialog.asksaveasfile()
    print(file)
    select = e.widget["text"]
    if select == "s1" :
        s1.set(file)
    else:
        s2.set(file)
    # print(file2)
    # print(file)

def ctext(e):
    readtext = t1.get("1.0","end-1c")
    cuttext = readtext.split(',')
    print(cuttext)


lb1 = Label(gui,text = "Select Source File :",width=20,anchor = E)
lb1.config(font = setfont)
lb1.grid(row = 0,column = 0,ipadx = 5,ipady = 5)

s1 = StringVar()
input1 = Label(gui,textvariable = s1,width=30,anchor = W)
input1.grid(row = 0,column = 1)

bt1 = Button(gui,text = "s1")
bt1.bind('<Button-1>', testdata)
bt1.grid(row = 0,column = 2)

lb2 = Label(gui,text = "Select Destination File :",width=20,anchor = E)
lb2.config(font = setfont)
lb2.grid(row = 1,column = 0,ipadx = 5,ipady = 5)

s2 = StringVar()
input2 = Label(gui,textvariable = s2,width=30,anchor = W)
input2.grid(row = 1,column = 1)

bt2 = Button(gui,text = "s2")
bt2.bind('<Button-1>', testdata)
bt2.grid(row = 1,column = 2)


t1 = Text(gui,height=10,width = 30,padx = 10 ,pady = 10,highlightcolor = "red")
t1.grid(row = 2,column = 0)

bt3 = Button(gui,text = "s2")
bt3.bind('<Button-1>', ctext)
bt3.grid(row = 2,column = 2)

gui.mainloop()