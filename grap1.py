import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import random
import datetime
from itertools import count
import seaborn as sns
import sqlite3
import pyodbc
import numpy as np
from time import sleep
import serial

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
	sql = """ SELECT * FROM test.dbo.pcbtest	"""
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
	root = Tk()
	con_string = """Driver={SQL Server};
				Server=127.0.0.1;
				Database = test;
				UID = admin;
				PWD = admin;
				"""
	sqlstr = """ select * from test.dbo.xx	"""
	conn = pyodbc.connect(con_string)
	# url = 'https://github.com/prasertcbs/tutorial/raw/master/mpg.csv'
	# df=pd.read_csv(url)
	df = pd.read_sql(sql = sqlstr,con = conn)
	# plt.style.use('seaborn-darkgrid')
	plt.style.use('fivethirtyeight')
	fig,ax = plt.subplots(1,1,figsize=(18,8),sharey=True,dpi = 50)
	bar1 = FigureCanvasTkAgg(fig, root)
	bar1.get_tk_widget().grid(row = 0,column = 0,padx = 10,pady = 10)
	
	# sns.countplot(x ='year',data = df ,hue = 'class',ax=ax)
	# sns.barplot(x='fname',y ='age',data = df ,saturation =8,ax=ax[1])
	x_val = []
	y_val = []
	z_val = []
	index = count()
	def autolabel(rect):
		# for r in rect:
		# 	height = r.get_height()
		# 	ax.annotate('{}'.format(height),
		# 					xy=(r.get_x() + r.get_width()/2,height),
		# 					xytext = (0,3),
		# 					textcoords = "offset points",
		# 	
		# 				ha = "center",va = "center")
		for r in rect:
			xdata,ydata = r.get_data()
			c = len(ydata)-1
			for i,d in enumerate(ydata):
				ax.annotate('{}'.format(d),
					xy=(i,d),
					xytext = (0,3),
					textcoords = "offset points",
					ha = "center",va = "center")

	def serialget():
		ser = serial.Serial(port='COM4',baudrate=9600,bytesize=8,parity='N',stopbits=1)
		# ser.open()
		a = ser.readline()
		ser.close()
		print(a)
		# sleep(1)
		return int(a)

		
	def animate(i):
		# df = pd.read_sql(sql = sqlstr,con = conn)
		dt = datetime.datetime.now().strftime("%H:%M:%S")
		# srg = serialget()
		x_val.append(dt)
		y_val.append(random.randint(10,40))
		z_val.append(random.randint(20,50))
		if len(x_val) > 20:
			del x_val[0]
			del y_val[0]
			del z_val[0]
		ax.cla()
		ax.set_ylim(0,60)
		ax.set_yticks(np.arange(0,65,2.5))
		rect1 = ax.plot(x_val,y_val,label = 'chanel1')
		rect2 = ax.plot(x_val,z_val,label = 'chanel2')
		ax.legend(loc = 'upper right')
		autolabel(rect1)
		autolabel(rect2)
		# df.plot(x='fname' ,y =['money','age'],kind = 'bar',legend = True,ax = ax)

	ani = FuncAnimation(fig,animate,interval = 1000)

	# use plt with normal case
	# x1 = np.arange(len(df['fname']))
	# wx = 0.35
	# ax[0].bar(x1-wx/2,df['money'], wx,label = 'money')
	# ax[0].bar(x1+wx/2,df['age'], wx,label = 'age')
	# ax[0].set_xticks(x1)
	# ax[0].set_xticklabels(df['fname'])

	headlist = df.columns
	tree = ttk.Treeview(root, column=tuple(np.arange(len(headlist))), show='headings')
	for r in range(len(headlist)):
		tree.column(f"{r}", anchor=CENTER, width = 80)
		tree.heading(f"{r}", text=headlist[r])
	tree.grid(row = 1,column = 0,padx = 10,pady = 10)
	for i in df.values.tolist():
		tree.insert(parent='', index='end',values=i[0:])

	def deldata(e):
		tree.delete(*tree.get_children())


	# str1 = StringVar()
	# ct = CutTextbox(root,relief='flat',highlightcolor='red',highlightthickness = 2)
	# ct.grid(row = 2,column = 1)

	# tb1 = Text(root,highlightcolor='red',highlightthickness = 2)
	# tb1.grid(row = 3,column = 1)
	# plt.tight_layout()
	fig.tight_layout()
	root.mainloop()



if __name__=='__main__':
	# in1 = int(input("Age :"))
	# demo1(in1)
	demo2()
	# demo3()
	
	






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