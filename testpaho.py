import paho.mqtt.client as mqtt
import time
import snap7
import struct

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


if __name__ == "__main__":
    runpaho()