import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
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

	# data1 = {'Country': ['US','CA','GER','UK','FR'],
    #      'GDP_Per_Capita': [45000,42000,52000,49000,47000]
    #     }
	# df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])

	# data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
    #      'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    #     }
	# df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])	


	root = Tk()
		
	# def add1(e):
	# 	(data1['GDP_Per_Capita'])[0] += 1000
	# 	val = (data1['GDP_Per_Capita'])[0]
	# 	result.set(val)
	# 	print(val)
	con_string = """Driver={SQL Server};
				Server=127.0.0.1;
				Database = test;
				UID = admin;
				PWD = admin;
				"""
	sqlstr = """ select * from test.dbo.xx	"""
	conn = pyodbc.connect(con_string)
	df = pd.read_sql(sql = sqlstr,con = conn,index_col = 'id')
	figure1 = plt.Figure(figsize=(6,5), dpi=100)
	ax1 = figure1.add_subplot(111)
	bar1 = FigureCanvasTkAgg(figure1, root)
	bar1.get_tk_widget().grid(row = 0,column = 0)
	df[['fname','money']].plot(kind = 'bar',legend = True,ax=ax1)
	print(df.iloc[df['age'].values,[0,3]])

	tree = ttk.Treeview(root, column=(1,2,3,4,5,6), show='headings')
	# tree.column("#1", anchor=CENTER)
	tree.heading("#1", text="ID")
	# tree.column("#2", anchor=CENTER)
	tree.heading("#2", text="FNAME")
	# tree.column("#3", anchor=CENTER)
	tree.heading("#3", text="LNAME")
	tree.heading("#4", text="AGE")
	tree.heading("#5", text="TOY")
	tree.heading("#6", text="MONEY")
	tree.grid(row = 0,column = 1)
	# tree.insert(parent='', index='end', iid=0, text="Label", values=("Hello", "Second Col", "Third Col"))
	# for i,v in enumerate(df):
	# 	# print(f"{i} {v}")
	# 	tree.insert('', END, values=df.iloc[i,:].tolist())
		# tree.insert('', i, text=rowLabels[i], values=df.iloc[i,:].tolist())
			# result = IntVar()
	# lb1 = Label(root,textvariable = result, height = 2,width = 8, bg = "yellow")
	# lb1.grid(row = 1,column = 0)

	# bt1 = Button(root,text = "enter", width = 20)
	# bt1.bind('<Button-1>', add1)
	# bt1.grid(row = 1,column = 1)



	# figure2 = plt.Figure(figsize=(5,4), dpi=100)
	# ax2 = figure2.add_subplot(111)
	# line2 = FigureCanvasTkAgg(figure2, root)
	# line2.get_tk_widget().grid(row = 0,column = 1)
	# df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
	# df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
	# ax2.set_title('Year Vs. Unemployment Rate')


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