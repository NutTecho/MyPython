import paho.mqtt.client as mqtt
import time
import snap7
import struct
# from snap7.util import get_bool,get_dword,get_int,get_real
# from snap7.util import set_bool,set_int,set_real,set_dword
# from snap7.snap7types import areas,cpu_statuses,S7WLBit,S7WLByte,S7WLDWord,S7WLReal,S7WLWord
from snap7.util import * 
from snap7.snap7types import *
c = snap7.client
# The callback for when the client receives a CONNACK response from the server.
def on_connect1(self,client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    self.subscribe([("test/MQTT",0),("test/haha",1)])


def on_publish(self,client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    self.publish("test/MQTT","thailand",0)

def on_message(client, userdata, msg):
    print(msg.topic+" "+ msg.payload.decode("utf-8","strict"))

def runpaho():
    client = mqtt.Client()
    client.username_pw_set(username="mymqtt",password="myraspi")
    client.on_connect = on_connect1
    # client.on_connect = on_publish
    client.on_message = on_message
    client.connect(host="192.168.137.4",port =1883, keepalive=60,bind_address="")
    client.loop_forever()


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype == S7WLBit:
        return get_bool(result,0,bit)
    elif datatype == S7WLByte or datatype ==S7WLWord:
        return get_int(result,0)
    elif datatype == S7WLReal:
        return get_real(result,0)
    elif datatype == S7WLDWord:
        return get_dword(result,0)
    else:
        return None  

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.write_area(areas['MK'],0,byte,datatype)
    if datatype == S7WLBit:
        return set_bool(result,0,bit,value)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return set_int(result,0,value)
    elif datatype == S7WLReal:
        return set_real(result,0,value)
    elif datatype == S7WLDWord:
        return set_dword(result,0,value)
    else:
        return None  

def runsiemens():
    xplc = c.Client()
    xplc.connect('192.168.137.5',0,1)
    print(xplc.get_connected)

    # WriteMemory(xplc,0,0,S7WLBit,1)
    # xplc.db_write(1,31,120,1)

if __name__ == "__main__":
    runsiemens()
    # runpaho()