import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import seaborn as sns
import sqlite3
import pyodbc
import numpy as np

def demo1(a):
	try:
		with sqlite3.connect("E:/sql3/test.sqlite")as con:
			con.row_factory = sqlite3.Row
			sql_cmd = """
			select *
			from t1
			where age > ?
			"""
			c1 = con.execute(sql_cmd,[a])
			for row in c1:
				# print(row)
				print("{} {} {}".format(row["id"],row["name"],row["age"]))
	except Exception as er :
		print('Error -> {}'.format(er))

def demo2():
	con_string = """Driver={SQL Server};
				Server=127.0.0.1;
				Database = test;
				UID = client1;
				PWD = nutert0405;
				"""
	sql = """ SELECT * FROM test.dbo.xx	"""
	try:
		with pyodbc.connect(con_string) as con:
			c1 = con.cursor()
			c1.execute(sql)
			for row in c1:
				print(row)
			
	except Exception as er :
		print('Error -> {}'.format(er))
	# finally:
		# con.close()
	
def demo3():

	class HoverButton(Button):
		def __init__(self,master,**kw):
			Button.__init__(self,master = master,**kw)
			self.defaultbackground = self['background']
			self.bind('<Enter>',self.hoveron)
			self.bind('<Leave>',self.hoveroff)

		def hoveron(self,e):
			self['background'] = self['activebackground']

		def hoveroff(self,e):
			self['background'] = self.defaultbackground

	class CutTextbox(Entry):
		def __init__(self,master,**kw):
			Entry.__init__(self,master = master,**kw)
			self.bind('<Return>',self.cutting)

		def cutting(self,e):
			self.keepdata = e.widget.get()
			if(len(self.keepdata) > 10):
				self.delete(0,END)
				self.insert(END,self.keepdata[0:3])

	root = Tk()
	con_string = """Driver={SQL Server};
				Server=127.0.0.1;
				Database = test;
				UID = admin;
				PWD = admin;
				"""
	sqlstr = """ select * from test.dbo.xx	"""
	conn = pyodbc.connect(con_string)
	url = 'https://github.com/prasertcbs/tutorial/raw/master/mpg.csv'
	df=pd.read_csv(url)
	# df = pd.read_sql(sql = sqlstr,con = conn)
	fig,ax = plt.subplots(1,1,figsize=(6,3),sharey=True)
	bar1 = FigureCanvasTkAgg(fig, root)
	bar1.get_tk_widget().grid(row = 0,column = 0,padx = 10,pady = 10)
	# df.plot(x='fname' ,y =['money','age'],kind = 'bar',legend = True,ax=ax[0],color = ['r','b'])
	sns.countplot(x ='year',data = df ,hue = 'class',ax=ax)
	# sns.barplot(x='fname',y ='age',data = df ,saturation =8,ax=ax[1])

	# use plt with normal case
	# x1 = np.arange(len(df['fname']))
	# wx = 0.35
	# ax[0].bar(x1-wx/2,df['money'], wx,label = 'money')
	# ax[0].bar(x1+wx/2,df['age'], wx,label = 'age')
	# ax[0].set_xticks(x1)
	# ax[0].set_xticklabels(df['fname'])

	headlist = df.columns
	tree = ttk.Treeview(root, column=(0,1,2,3,4,5,6,7,8,9,10,11), show='headings')
	for r in range(len(headlist)):
		tree.column(f"{r}", anchor=CENTER, width = 80)
		tree.heading(f"{r}", text=headlist[r])
	tree.grid(row = 0,column = 1,padx = 10,pady = 10)
	for i in df.values.tolist():
		tree.insert(parent='', index='end',values=i[0:])

	def deldata(e):
		tree.delete(*tree.get_children())


	bt1 = HoverButton(root,text = "enter", width = 20, activebackground = 'red')
	bt1.bind('<Button-1>', deldata)
	bt1.grid(row = 1,column = 1)

	# str1 = StringVar()
	ct = CutTextbox(root)
	ct.grid(row = 2,column = 1)

	fig.tight_layout()
	root.mainloop()



if __name__=='__main__':
	# in1 = int(input("Age :"))
	# demo1(in1)
	# demo2()
	demo3()
	
	






# in1 = 8
# y1 = []
# y2 = []
# for i in range(in1):
# 	a = random.randint(1,6)
# 	b = random.randint(1,6)
# 	y1.insert(i,a)
# 	y2.insert(i,b)
# print(y1,y2)
# x = range(in1)
# plt.plot(x,y1,color="red",linewidth=1,Linestyle = "dotted",label="a1")
# plt.plot(x,y2,color="blue",linewidth=1,Linestyle = "dashed",label="a2")
# plt.xlabel("testX")
# plt.ylabel("testY")
# plt.title("testGraph")
# plt.legend()
# plt.grid()
# plt.show()