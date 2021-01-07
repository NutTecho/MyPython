from tkinter import *
from tkinter import ttk


root = Tk()
root.title("test")
# root.geometry("400x600")
root.option_add("*Font","consolas,20")


myMenu = Menu(root)
file_menu = Menu(myMenu,tearoff=0)
myMenu.add_cascade(label="File",menu=file_menu)
myMenu.add_cascade(label = "save")
root.config(menu=myMenu)

man_c = 0
women_c = 0
total_c = 0

def xclick():
	t = "hello" + c1.get()
	label1 = Label(root,text = t)
	e.delete(0,'end')
	label1.pack(pady = 10)
	myFrame.pack(fill="both",expand=1)
	

def comboClick(event):
	if d1.get()=='Friday':
		label1=Label(root,text = 'Yes! that''s Friday').pack(pady = 10)
	else:
		label1=Label(root,text = d1.get()).pack(pady = 10)

def man_click():
	global man_c
	global total_c
	man_c +=1
	total_c +=1
	man_count.set(man_c)
	total_count.set(f'total = {total_c}')

def women_click():
	global women_c
	global total_c
	women_c +=1
	total_c -=1
	women_count.set(women_c)
	total_count.set(f'total = {total_c}')


def on_click(e):
	global women_c
	global total_c
	global man_c
	gender = e.widget["text"]
	if gender == "MAN":
		man_c +=1
		total_c +=1
		man_count.set(man_c)
	else:
		women_c +=1
		total_c -=1
		women_count.set(women_c)

	total_count.set(f'total = {total_c}')

# --------------frame-------------------
# myFrame = Frame(root,width=200,height=200,bg="red")

# ----------Entry box------------------------
# e = Entry(root,width = 10,font = ('Helvetica',30))
# e.pack(padx = 10,pady = 10)


# -------Button------------------------------------
# b1 = Button(root,text = "ENTER",command = xclick)
# b1.pack(pady = 20)

# images = ["man","women"]
# color = ["sky blue","hot pink"]
# caption = ["MAN","WOMEN"]
# Photo = [PhotoImage(file = f'{image}.png') for image in images]
# for i in range(len(Photo)):
# 	B1 = Button(root,text = caption[i],image = Photo[i],bg = color[i],compound = TOP).pack(side = LEFT)

# Photo1 = PhotoImage(file = "man.png",width = 100,height = 100)
# Photo2 = PhotoImage(file = "women.png")

# B1 = Button(root,text = "MAN",compound = BOTTOM,image = Photo1,bg = "sky blue")
# B1.grid(row = 1,column = 1)
# B1.bind("<Button-1>",on_click)

# B2 = Button(root,text = "WOMAN",compound = BOTTOM,image = Photo2,bg = "hot pink")
# B2.grid(row = 1,column = 2)
# B2.bind("<Button-3>",on_click)

man_count = IntVar()
women_count = IntVar()
total_count = StringVar()

Label(root,textvariable = man_count,bg = "orange",width = 5).grid(row = 2 ,column = 1)
Label(root,textvariable = women_count,bg = "orange",width = 5).grid(row = 2,column = 2)
Label(root,textvariable = total_count,bg = "orange",width = 10).grid(row =3,columnspan = 5)

#-------------option------------------------ 
op1 = [
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thuesday",
		"Friday"]
c1 = StringVar()
c1.set(op1[0])
d1 = OptionMenu(root,c1,*op1)
d1.grid(row = 4,column = 1)

# ---------------commbobox-------------------
# myCombo = ttk.Combobox(root,value = op1)
# myCombo.current(0)
# myCombo.bind("<<ComboboxSelected>>",comboClick)
# myCombo.pack(pady = 40) 

def s_click(e):
	e.widget["bg"] = "red"

d = {"Thai":"TH","Japan":"JP","Korea":"KR","Chinese":"CH"}
cnt = StringVar()
cnt.set("Thai")
n_row = 0
for k,v in d.items():
	r = Radiobutton(root,text = k,value = v,indicatoron = False,variable = cnt,width = 11,anchor = W,bg = "gold")
	r.grid(row = n_row+5 ,column = 1) 
	r.bind("<Button-1>",s_click)
	n_row+=1

def on_drag(e):
	color_hex = f'#{color_code[0].get():02X}{color_code[1].get():02X}{color_code[2].get():02X}'
	tcolor.set(color_hex)
	lb_color["bg"] = color_hex

color_code = []
rgb = ["red","green","blue"]
for i,c in enumerate (rgb):
	colorpick1 = Label(root,text = c,fg = c,anchor = W)
	colorpick1.grid(row =  10+i,sticky = "sw")
	sc = Scale(root,from_ = 0 ,to = 255,orient = HORIZONTAL,length = 200,width = 30)
	sc.grid(row = 10+i,column = 1)
	sc.set(128)
	sc.bind('<B1-Motion>',on_drag)
	sc.bind('<Button-1>',on_drag)
	color_code.append(sc)

tcolor = StringVar()
lb_color = Label(root,textvariable = tcolor,width = 30,height = 5)
lb_color.grid(row = 20,columnspan = 3)

root.mainloop()

