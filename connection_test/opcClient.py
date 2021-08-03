from opcua import Client
from opcua import ua
import  time

url = "opc.tcp://localhost:4840"
client = Client(url)
client.connect

# root = client.get_root_node()
# print(root)
# obj = client.get_objects_node()
# print(obj)
# serv = client.get_server_node()
# print(serv)

# test = client.get_node(nodeid=85)
# print(test)

while True:
	
	Temp = client.get_node("ns=2;i=2")
	Temperature = Temp.get_value
	print(Temperature)

	# Pressure = Press.get_value()
	# print(Press)

	xtime = client.get_node("ns=2;i=1")
	xtimevalue = xtime.get_value
	print(xtimevalue)

	time.sleep(1)