from opcua import Server
from random import  randint
import datetime
import time
import sys

sys.path.insert(0,"..")
server = Server()
url = "opc.tcp://localhost0.0.0.0:4840"
server.set_endpoint(url)

# uri = "http://examples.freeopcua.github.io"
name = "OPC_SIMULATION_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()
param = node.add_object(addspace,"Parameters")

Temp = param.add_variable(addspace,"Temperature",0)
Time = param.add_variable(addspace,"Time",0)

Temp.set_writable()
Time.set_writable()

server.start
print("Server start as {}".format(url))

while  True:
	Temperature = randint(10,50)
	xTime = datetime.datetime.now()
	print(Temperature,xTime)

	Temp.set_value(Temperature)
	Time.set_value(xTime)

	time.sleep(2)

