import pyodbc
import serial
import socket
import pandas as pd
import openpyxl
from time import sleep
import paho.mqtt.client as mqtt
con_string = """Driver={SQL Server};
				Server=127.0.0.1;
				Database = test;
				UID = admin;
				PWD = admin;
				"""
def pdtest1():
	
	sqlstr = """ select * from test.dbo.xx	"""
	conn = pyodbc.connect(con_string)
	df = pd.read_sql(sql = sqlstr,con = conn,index_col = 'id')
	print(df)

def readexcel():

	excelpath = "test.xlsx"
	# df = pd.read_excel(excelpath,sheet_name="Sheet1",header=2,index_col='id')
	# df1 = pd.read_excel(excelpath,sheet_name="Sheet2",header=2,index_col='id')
	# full = pd.concat([df,df1],axis=0)
	# print(full)
	# df.to_excel('output.xlsx',sheet_name='Sheet1',index = False)

	# sheet = pd.ExcelFile(excelpath)
	# print(sheet.sheet_names)
	# df = sheet.parse(sheet_name=,header = 3)
	# print(df)
	fulldata = []
	with pd.ExcelFile(excelpath) as workbook:
		for sheet in workbook.sheet_names:
			# fulldata[sheet] = workbook.parse(sheet,header=3)
			df = pd.read_excel(excelpath,sheet_name=sheet,header = 2)
			fulldata.append(df)
	# df = pd.DataFrame(fulldata)
	comb = pd.concat(fulldata,axis=0)
	comb.to_excel('output.xlsx',sheet_name='Sheet1',index = False)
	print(comb)
	




def create_table():
	sql = """
			create table t1(
			id int
			name nvarchar)
			"""
	with pyodbc.connect(con_string) as con:
		c1 = con.execute(sql)
		for row in c1:
			print(row)

def select_table():
	sql = """ 
		select * from TPP where DAY_TIME > 2020-02-28
	"""
	with pyodbc.connect(con_string) as con:
		c1 = con.execute(sql)
		for row in c1:
			print(row)

def serialtest():
	ser = serial.Serial(port='COM4',baudrate=9600,bytesize=8,parity='N',stopbits=1)
	print(ser)
	# ser.open()
	print(ser.is_open)
	ser.write(b"open reading")
	while(True):
		a = ser.readline();
		print(a)
		sleep(1)
	# ser.close()

def publishmqtt():
	host = "broker.emqx.io"
	port = 1883
	client = mqtt.Client()
	client.connect(host,port,60)

	client.publish("test/MQTT","haha")
	client.publish("test/haha","banana")
	

def sockettest():
	sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	# sk.bind(("",port))


if __name__=='__main__':
	# pdtest1()
	# select_table()
	# serialtest()
	# testmqtt()
	# publishmqtt()
	readexcel()