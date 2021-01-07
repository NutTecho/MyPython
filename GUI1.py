from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import colorchooser
from tkinter import filedialog
import sys


def mhello():
    print("hello")


def hello(event):
    # messagebox.showwarning(title="information", message="Hello User")
    status = messagebox.askyesno(title="Question", message="What your name")
    if status > 0:
        sys.exit()


def fColor(event):
    myColor = colorchooser.askcolor()
    L2 = Label(text=myColor).pack()


def fOpen(event):
    # filedialog.askopenfile()
    # file = filedialog.askdirectory()
    file2 = filedialog.askopenfilename(title = "test",filetype = [('Excel')])
    # saveFile = filedialog.asksaveasfile()
    print(file2)
    # print(file)


gui = Tk()
gui.geometry("450x500")

L1 = Label(text="NUT_TECHOSAKONDEE", fg="#000", bg="pink", font=("Arial Bold", 20)).pack()

B1 = Button(text="Enter", command=mhello)
B1.bind('<Button-1>', hello)
B1.pack()

B2 = Button(text="Color")
B2.bind('<Button-1>', fColor)
B2.pack()

B3 = Button(text="File")
B3.bind('<Button-1>', fOpen)
B3.pack()

#สร้างกล่องใส่ข้อความ
T1 = Entry(bd = 5).pack()

#สร้างปุ่มตัวเลือก
R1 = Radiobutton(text="Male", value=1).pack()
R2 = Radiobutton(text="female", value=2).pack()

#สร้าง Spin Box
S1 = Spinbox(from_ = 1,to = 10).pack()

#สร้าง List Box
Lb1 = Listbox()
Lb1.insert(1,"Hello")
Lb1.insert(2,"Bye")
Lb1.pack()

#สร้าง Slider
Sl1 = Scale(orient = HORIZONTAL,width = 20,from_ = 0,to = 100,length=300,tickinterval = 10).pack()

#OptionMenu
t1 = [
    "thailand",
      "japan",
      "canada",
      "russia"]
c1 = StringVar()
c1.set(t1[0])
D1 = OptionMenu(gui,c1,*t1).pack()

# Combobox
data = ['a','b','c','d','e']
c1 = ttk.Combobox(gui,value = data,justify = "center",state = "readonly")
c1.pack()
c1.current(0)

#สร้าง menu
menubar = Menu(gui)
fileMenu = Menu(menubar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Import")
fileMenu.add_command(label="Export")
menubar.add_cascade(label="File", menu=fileMenu)
gui.config(menu=menubar)

# สร้าง tab control
tab_control = ttk.Notebook(gui)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1,text = 'first')
tab_control.add(tab2,text = 'second')
lb1 = Label(tab1,text = "hello",padx = 5,pady = 5).pack()
lb2 = Label(tab2,text = "Bye").pack()

tab_control.pack(expand = 1,fill='both')

gui.mainloop()
