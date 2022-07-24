from opcua import Client
import  time

url = "opc.tcp://localhost:4841"
client = Client(url)
client.connect()
client.load_type_definitions()

root = client.get_root_node()
print("Root node is: ", root)
objects = client.get_objects_node()
print("Objects node is: ", objects)

uri = "http://examples.freeopcua.github.io"
idx = client.get_namespace_index(uri)

myvar = root.get_child(["0:Objects", "{}:MyObject".format(idx), "{}:MyVariable".format(idx)])
obj = root.get_child(["0:Objects", "{}:MyObject".format(idx)])
print("myvar is: ", myvar)

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