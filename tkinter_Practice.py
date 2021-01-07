from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("test")
root.geometry("200x200")
root.minsize(400,400)
root.maxsize(600,600)
# root.resizable(height = False,width = False)
root.option_add("*Font","consolas,20")

# for x in range(3):
#     Grid.columnconfigure(root,x,weight=1)

# for y in range(3):
#     Grid.rowconfigure(root,y,weight=1)
# Frame1 = Frame(root)
# Frame1.pack(side = "left",fill = "both")

# a1 = Label(root,text = "Hello",bg="red",fg="white").pack(side = "top",fill = "x")
# a2 = Label(root,text = "Hello",bg="blue",fg="white").pack(side = "left",fill = "y")
# a3 = Label(Frame1,text = "Hello",bg="green",fg="white").pack(side = "top",fill = "both",expand = True)
# a4 = Label(Frame1,text = "Hello",bg="pink",fg="white").pack(side = "bottom",fill = "both",expand = True)

# B = Button(root,text = "B",bg = "yellow")
# C = Button(root,text = "C",bg = "yellow")
# A = Button(root,text = "A",bg = "yellow")
# D = Button(root,text = "D",bg = "yellow")
# E = Button(root,text = "E",bg = "yellow")
# F = Button(root,text = "F",bg = "yellow")
# G = Button(root,text = "G",bg = "yellow")
# H = Button(root,text = "H",bg = "yellow")
# I = Button(root,text = "I",bg = "yellow")

# A.grid(row = 0,column = 0)
# B.grid(row = 0,column = 1)
# C.grid(row = 0,column = 2)
# D.grid(row = 1,column = 0)
# E.grid(row = 1,column = 1)
# F.grid(row = 1,column = 2)
# G.grid(row = 2,column = 0)
# H.grid(row = 2,column = 1)
# I.grid(row = 2,column = 2)

# A.place(x=100,y=100)
# A.place(relx = 0.5,rely = 0.5)
# A.place(width = 100,height = 100,relwidth = 0.5,relheight = 0.5)
e1 = Entry(root,show = "*").pack()

data = ['a','b','c','d','e']
c1 = ttk.Combobox(root,value = data,justify = "center",state = "readonly")
c1.pack()
c1.current(0)

def openFile():
    # file = filedialog.askdirectory()
    file2 = filedialog.askopenfilename(title = "test",filetype = [('Excel')])
    # saveFile = filedialog.asksaveasfile()
    print(file2)
    # print(file)

Button(root,text = "test",command = openFile).pack()



root.mainloop()