from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import colorchooser
from tkinter import filedialog
from shutil import copyfile,copy2
import os

class Application(Frame):
    def __init__(self,root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.root.title("Application")
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(0, weight=1)
        self.root.geometry("800x400")
        # self.root.config(background="green")
        # self.root.Font(family="Arial", size=16, weight="bold", slant="italic")
        setfont = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self.Frame1 = Frame(self.root,bg = "pink")
        self.Frame2 = Frame(self.root,bg = "yellow")
        self.Frame3 = Frame(self.root,bg = "skyblue")
       
        self.subFrame1_1 = Frame(self.Frame1)
        self.Frame1.pack(side = "left",fill = "both",expand = "True")
        self.Frame2.pack(side = "right",fill = "both",expand = "True")
        self.Frame3.pack(side = "top",fill = "both",expand = "True")
        self.subFrame1_1.grid(row = 3,column = 1)

        self.lb1 = Label(self.Frame1,text = "Select Source File :",width=15,anchor = E)
        self.lb1.config(font = setfont)
        self.lb1.grid(row = 0,column = 0,padx = 5,pady = 5)

        self.s1 = StringVar()
        self.input1 = Listbox(self.Frame1,width=40,height = 20)
        self.input1.grid(row = 1,column = 0,rowspan = 3, padx = 5,pady = 5)

        self.btAdd = Button(self.subFrame1_1,text = "add",width=10)
        self.btAdd.bind('<Button-1>', self.openselect)
        self.btAdd.grid(row = 0,column = 0)

        self.btDel = Button(self.subFrame1_1,text = "delete",width=10)
        self.btDel.bind('<Button-1>', self.delselect)
        self.btDel.grid(row = 1,column = 0)

        self.btClear = Button(self.subFrame1_1,text = "clear",width=10)
        self.btClear.bind('<Button-1>', self.clearall)
        self.btClear.grid(row = 2,column = 0)

        self.lb2 = Label(self.Frame2,text = "Select Destination File :",width=20,anchor = E)
        self.lb2.config(font = setfont)
        self.lb2.grid(row = 0,column = 0,columnspan = 2,padx = 5,pady = 5)

        self.s2 = StringVar()
        self.input2 = Label(self.Frame2,textvariable = self.s2,width=30,height = 2,anchor = W)
        self.input2.grid(row = 1,column = 0)

        self.bt2 = Button(self.Frame2,text = "des",width = 10)
        self.bt2.bind('<Button-1>', self.openselect)
        self.bt2.grid(row = 1,column = 1)

        self.btCopy = Button(self.Frame2,text = "Copy",width = 10)
        self.btCopy.bind('<Button-1>', self.copyto)
        self.btCopy.grid(row = 2,column = 1)

        self.textb1 = Listbox(self.Frame2,height=10,width = 30)
        self.textb1.grid(row = 2,column = 0,padx = 5,pady = 5)

    def openselect(self,e):
        # filedialog.askopenfile()
        self.filepath = filedialog.askdirectory()
                
        # file2 = filedialog.askopenfilename(title = "test",filetype = [('Excel')])
        # saveFile = filedialog.asksaveasfile()
        # print(file)
        self.select = e.widget["text"]
        if self.select == "add" :
             self.arrpath = os.listdir(self.filepath)
             for i,r in enumerate(self.arrpath):
                # self.textb1.insert(END,r + '\n')
                self.input1.insert(i,self.filepath+'/'+ r)
        else:
            self.s2.set(self.filepath)
            self.arrpath = os.listdir(self.filepath)
            for i,r in enumerate(self.arrpath):
                # self.textb1.insert(END,r + '\n')
                self.textb1.insert(i,self.filepath+'/'+ r)
                # self.textb1.insert(END,r + '\n')


    def delselect(self,e):
        self.index = self.input1.curselection()
        print(self.index)
        self.input1.delete(self.index[0])

    def clearall(self,e):
        self.input1.delete(0,END)

    def copyto(self,e):
        allsource = self.input1.get(0,END)
        alldes = self.textb1.get(0,END)
        print(allsource)
        print(alldes)
        try:
            for source in allsource:
                for des in alldes:
                    copy2(source,des)
        except expression as e:
            print("Error -> {e}")

       
 

app = Application(Tk())
app.root.mainloop()