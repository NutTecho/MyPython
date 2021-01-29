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
root.geometry("600x600")
x_list = []

def checkdate(e):
    # row = en.grid_info()['row']
    # print(row)
    rec = e.widget.get()
    # print(rec)
    index = int(e.widget.name)
    # print(index)
    tar = partitem[index].get()
    print(index,rec,tar)
    if rec == tar:
        
        stat[index]["text"] = "OK"
        idlist[index]["bg"] = "lightgreen"
        partitem[index]["bg"] = "lightgreen"
        stat[index]["bg"] = "lightgreen"
    else:
        stat[index]["text"] = "NG"
        idlist[index]["bg"] = "indianred"
        partitem[index]["bg"] = "indianred"
        stat[index]["bg"] = "indianred"

        
            # x_list[0].set("settest")
          

idlist = []
partitem = []
stat = []


for i in range(11):
    
    idnum = Entry(root,relief='solid', width = 15,borderwidth=1,font = "consolas 20",justify = "center")
    idnum.name = f"{i}"
    idnum.bind('<Return>',checkdate)
    idnum.grid(row = i,column = 0,sticky = "NEWS")

    partname = Entry(root,relief='solid',width = 15 ,font = "consolas 20",justify = "center")
    partname.name =f"{i}"
    partname.grid(row = i,column = 1,sticky = "NEWS")

    status = Label(root,relief='solid',width = 5,borderwidth=1 ,font = "consolas 20")
    status.name = f"{i}"
    status.grid(row = i,column = 2,sticky = "NEWS")

    idlist.append(idnum)
    partitem.append(partname)
    stat.append(status)

root.mainloop()