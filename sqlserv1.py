import pyodbc
import serial
import socket
from time import sleep
import paho.mqtt.client as mqtt
con_string = """driver=odbc Driver 13 for SQL Server;
				server=127.0.0.1;
				database = test;
				username = admin;
				password = admin;
				"""

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
	# select_table()
	serialtest()
	# testmqtt()
	# publishmqtt()