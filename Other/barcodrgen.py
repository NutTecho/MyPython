import pandas as pd
import os
import xlrd
from tkinter import * 
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

worksheet = xlrd.open_workbook(os.path.join(sys.path[0],"test.xls"))
sheet = worksheet.sheet_by_name("Sheet1")

row_count = sheet.nrows
col_count = sheet.ncols

dictmodel = {}
for xrow in range(2,row_count):
    ID = sheet.cell(xrow,0).value
    FNAME = sheet.cell(xrow,1).value
    AGE = sheet.cell(xrow,2).value
    TOY = sheet.cell(xrow,3).value
    print(ID,FNAME,AGE,TOY)
    dictmodel[ID] = FNAME

namelist = list(dictmodel.values())

def showmodel(event):
    # getmodel = df['toy'][ df['fname'] == c1.get()].values[0]
    # print(getmodel)

    getmodel = dictmodel[c1.get()].values    
    model.set(getmodel)

    # qr.add_data(getmodel)
    # qr.make(fit=True)
    # imgqr = qr.make_image(fill_color="black", back_color="white")
    # imgqr.save("model.png")
    # img2 = ImageTk.PhotoImage(imgqr)
    # lb3.config(image = img2)
    # lb3.image = img2


root = Tk()
root.geometry("300x300")
root.title("test demo")
style = ThemedStyle(root)
style.set_theme("plastik")
# a = style.theme_names()
# print(a)
bg = style.lookup('TLabel', 'background')
fg = style.lookup('TLabel', 'foreground')
root.configure(bg=style.lookup('TLabel', 'background'))
style.configure('W.TCombobox',arrowsize = 60)
# lb_tasks.configure(bg=bg, fg=fg)

myfont = "Ubuntu 15 bold"
# df = pd.read_excel("test.xls",sheet_name = "Sheet1",skiprows=2)
# namelist = df['fname'].tolist()
# print(df)

lb1 = ttk.Label(root,text = "Select Model : ",font = myfont)
lb1.grid(row = 0,column = 0)

c1 = ttk.Combobox(root,value = namelist,width = 10,
style='W.TCombobox',font = myfont)
c1.current(0)
c1.bind("<<ComboboxSelected>>",showmodel)
c1.grid(row = 0,column = 1)

model = StringVar()
lb2 = ttk.Label(root,textvariable = model,font = myfont)
lb2.grid(row = 1,column = 0,columnspan = 2)

img = ImageTk.PhotoImage(file = "people.png")
lb3 = ttk.Label(root,image = img,width = 150)
lb3.grid(row = 2,column = 0,columnspan = 2,padx = 10,pady = 10)
# pic1 = Canvas(root,width = 100,height = 100)
# pic.grid(row = 0,column = 0,columnspan = 2)

root.mainloop()