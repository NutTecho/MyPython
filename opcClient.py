from opcua import Client
from opcua import ua
import  time


url = "opc.tcp://127.0.0.1:102"
client = Client(url)
client.connect

root = client.get_root_node()
print(root)
obj = client.get_objects_node()
print(obj)
serv = client.get_server_node()
print(serv)

# test = client.get_node(nodeid=85)
# print(test)

while True:
	
	Temp = client.get_node("ns=2;i=2")
	Temperature = Temp.get_value()
	print(Temperature)

	# Press = client.get_node("ns=2;i=3") 
	# Pressure = Press.get_value()
	# print(Press)

	TIME = client.get_node("ns=2;i=4")
	TIME_VALUE = TIME.get_value()
	print(TIME)

	time.sleep(1)