from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# test my programe123
gui = Tk()
gui.title("test")
gui.geometry("200x200")
gui.minsize(400,400)
gui.maxsize(600,600)
# gui.resizable(height = False,width = False)
gui.option_add("*Font","consolas,15")

def testdata(event):
    inp1.set(input1.get() +' '+ input2.get()+ ' '+c1.get())
    print(input1.get())
    messagebox.askyesno(title="Question", message=f"Your name is {input1.get()} {input2.get()}")

menubar = Menu(gui,tearoff = 0)
fileMenu = Menu(menubar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Import")
fileMenu.add_command(label="Export")
menubar.add_cascade(label="File", menu=fileMenu)
gui.config(menu=menubar)

tab_control = ttk.Notebook(gui)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1,text = 'Page1')
tab_control.add(tab2,text = 'Page2')
tab_control.pack(expand = 1,fill='both')

Frame1 = LabelFrame(tab1,text = "test data")
Frame2 = Frame(tab1,bg = "yellow")
Frame1.pack(side = "left",fill = "both",expand = "True")
Frame2.pack(side = "right",fill = "both",expand = "True")

lb1 = Label(Frame1,text = "hello",bg = "pink",width=15)
lb1.grid(row = 0,column = 0,ipadx = 5,ipady = 5,sticky = "sw")

input1 = Entry(Frame1,bd = 1,width=15)
input1.grid(row = 0,column = 1,sticky = "sw")

lb2 = Label(Frame1,text = "Bye",bg="yellow",width=15)
lb2.grid(row = 1,column = 0,ipadx = 5,ipady = 5)

input2 = Entry(Frame1,bd = 1,width=15)
input2.grid(row = 1,column = 1,sticky = "sw")

data = ['a','b','c','d','e']
c1 = ttk.Combobox(Frame1,value = data,justify = "center",state = "readonly",width=10)
c1.grid(row = 2,column = 1,sticky = "sw")
c1.current(0)

inp1 = StringVar()
output1 = Label(Frame1,textvariable = inp1,bg="green",width=15)
output1.grid(row = 3,column = 1,sticky = "sw")

B1 = Button(Frame1,text="Enter")
B1.bind('<Button-1>', testdata)
B1.grid(row = 4,column = 1,sticky = "sw")

lb3 = Label(Frame2,text = "hello",padx = 5,pady = 5,bg = "pink")
lb3.grid(row = 0,column = 0)

lb4 = Label(Frame2,text = "Bye",bg="yellow",padx = 5,pady = 5)
lb4.grid(row = 1,column = 0)

Lb1 = Listbox(Frame2)
Lb1.insert(1,"Hello")
Lb1.insert(2,"Bye")
Lb1.grid(row = 2,column = 0)


gui.mainloop()