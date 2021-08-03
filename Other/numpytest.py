import pandas as pd
import sqlite3
# import requests
from io import StringIO
from tkinter import *

def demo1():
	try:
		with sqlite3.connect("E:/sql3/test.sqlite") as con:
			con.row_factory = sqlite3.Row
			sql_cmd = """select * from t1 """
			cursur = con.execute(sql_cmd)
			for row in cursur:
				print("{} {} {}".format(row['id'],row['name'],row['age']))
	except Exception as e:
		print('Error -> {}'.format(e))

def select_data(param):
	con = sqlite3.connect("E:/sql3/test.sqlite")
	sql_cmd = """select * from t1"""
	df = pd.read_sql(sql_cmd,con)
	print(df)
	if param == "name":
		return df.name
	elif param == "age":
		return df.age
def test():
	url = 'https://spotifycharts.com/regional/global/daily/latest/download/regional-global-daily-latest.csv'
	# s = requests.get(url).text
	df = pd.read_csv(url)
	print(df.head())

def onReturn(e):

	# con = sqlite3.connect("E:/sql3/test.sqlite")
	# sql_cmd = """select * from t1 where age >?"""
	# df = pd.read_sql(sql_cmd,con,params='value')
	print("return")

def click(event):
	# t1.set("hello")
	s = t1.get()
	print(s)


def insert_data(param):
	try:
		with sqlite3.connect("E:/sql3/test.sqlite") as con:
			sql_cmd = """insert into t1(id,name,age) values(?,?,?)"""
			con.execute(sql_cmd,param)
	except exception as e:
		print('Error->{}'.format(e))

def interface():
	root = Tk()
	root.title('Test')
	root.option_add("*Font","consolas,20")
	root.geometry("200x300")

	t1 = StringVar()
	t1.set("Insert Number Here")
	a1 = Entry(root,textvariable = t1,width = 10)
	a1.focus_set()
	a1.bind("<Return>",onReturn)
	a1.grid(row = 1,column = 2)

	a2 = Entry(root,width = 10)
	a2.grid(row = 2,column = 2)
	
	b1 = Button(root,text = 'Enter',command = click)
	b1.grid(row = 3,column =2)


	op1 = select_data("name")
	c1 = StringVar()
	c1.set(op1[0])
	d1 = OptionMenu(root,c1,*op1)
	d1.grid(row = 1,column = 1)

	l1 = select_data("age")
	for i,c in enumerate(l1):
		r = Label(root,text = c,anchor = W)
		r.grid(row = 2+i,column=1)

	root.mainloop()


if __name__=="__main__":
	# test()
	# insert_data((6,'Mike',11))
	interface()
	# select_data()
	# demo1()
# data ={'day':['monday','tuesday','wensday'],
# 		'country':['Thailand','Japan','Korea'],
# 		'event':['Gift','Party','Game']
# }
# # df = pd.DataFrame(data)
# df = pd.read_csv('TPP.csv',nrows = 20,index_col = 'DAY_TIME',parse_dates = True)
# df['MACHINE_ID'] = 'TPP2'
# df['STATUS'] = 1
# df['DAY_TIME'] > 2020-02-24 7:50:00
# new_df = df.fillna({'MACHINE_ID':'NO','STATUS':0})
# new_df = df.fillna(methoh = 'ffill') #เติมค่าว่าง f = forward b = backward
# new_df = df.interpolate() #ระบุค่าประมาณระหว่างช่วงที่ว่างไว้
# new_df = df.dropna(how = 'all')
# new_df = df.loc[:,'MACHINE_ID','STATUS']
# print(df.columns[df.columns.str.contains('ER')])
# print(df.shape)
# print(df.STATUS.value_counts())
# print(df.describe())
# print(df.sample(frac = 0.5))
# print(df)
# print(df.nlargest(5,columns = 'STATUS'))
# print(pd.concat([df.head(),df.tail()]))