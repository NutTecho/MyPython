from tkinter import *
from tkinter import ttk

class CutTextbox(Entry):
		def __init__(self,master,**kw):
			Entry.__init__(self,master = master,**kw)
			self.bind('<Return>',self.cutting)
			# self.bind('<Enter>',self.hoveron)

		def cutting(self,e):
			self.keepdata = e.widget.get()
			if(len(self.keepdata) > 10):
				self.delete(0,END)
				self.insert(END,self.keepdata[0:3])

# def checkdata(e):
    # e.widget.get

root = Tk()
x_list = []

def checkdate(e):
    row = en.grid_info()['row']
    print(row)
    # x_list[0].set("settest")
          


for i in range(11):
    x_list.insert(i,StringVar())
    en = Entry(root,textvariable =  x_list[i],relief='flat',highlightcolor='red',highlightthickness = 2)
    en.bind('<Return>',checkdate)
    en.grid(row = i,column = 0)

    ct = CutTextbox(root,relief='flat',highlightcolor='red',highlightthickness = 2)
    ct.grid(row = i,column = 1)

    st = Entry(root,relief='flat',highlightcolor='red',highlightthickness = 2)
    st.grid(row = i,column = 2)

root.mainloop()