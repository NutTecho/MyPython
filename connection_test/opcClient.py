from opcua import Client , ua
import  time


def opc_test1():
	url = "opc.tcp://localhost:4843"
	client = Client(url)
	# client.set_security(policy=ua.SecurityPolicy.URI,
	# 				 certificate_path="certificate.pem",
	# 				 private_key_path="key.pem",
	# 				 mode=ua.MessageSecurityMode.SignAndEncrypt)

	client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.der,key.pem")
	# client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"
	client.session_timeout = 10000
	
	client.connect()
	# client.connect_and_get_server_endpoints()
	# client.load_client_certificate()	
	# client.load_private_key()
	# client.set_security_string( "Basic256,SignAndEncrypt,app_cert.der,app_cert_key.pem" )
	# tx = client.load_type_definitions()
	# print(tx)
	servnode = client.get_server_node()
	print("Server Node is : ",servnode)
	root = client.get_root_node()
	print("Root node is: ", root)
	objects = client.get_objects_node()
	print("Objects node is: ", objects)

	# get list of namespace
	arr_nm = client.get_namespace_array()
	print(arr_nm)

	# check name of in list namespace index
	arr_id = client.get_namespace_index("demo")
	print(arr_id)

	# list object return server object & node object with namespace id
	list_obj = objects.get_children()
	print(list_obj)

	# get variable in objects
	myobj = list_obj[1].get_children()
	print(myobj)

	list_var = [item.get_browse_name() for item in myobj]
	print(list_var)

	# myvar = root.get_child(["0:Objects", "{}:MyObject".format(idx), "{}:MyVariable".format(idx)])

	# obj = root.get_child(["0:Objects", "{}:MyObject".format(idx)])
	# print(obj)

	# print("myvar is: ", myvar)

	while True:
		
		for x in myobj:
			data = client.get_node(x).get_value()
			print(data)
		# Temperature = Temp.get_value()
		# print(Temperature)

		# Pres = client.get_node(ch1[1])
		# Pressure = Pres.get_value()
		# print(Pressure)

		# xtime = client.get_node(ch1[2])
		# xtimevalue = xtime.get_value()
		# print(xtimevalue)

		time.sleep(2)


class OPC_Event():
	def datachange_notification(self,node,val,data):
		print(f"node {str(node)} value is {str(val)}")

	def event_notification(self, event):
		print("Python: New event", event)


def opc_test2():
	url = "opc.tcp://localhost:4843"
	client = Client(url)

	# client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.der,key.pem")
	client.load_client_certificate("certificate.der")
	client.load_private_key("key.pem")
	client.application_uri = "demo"
	client.session_timeout = 10000
	client.connect()
	# client.load_type_definitions()

	servnode = client.get_server_node()
	print("Server Node is : ",servnode)
	root = client.get_root_node()
	print("Root node is: ", root)
	objects = client.get_objects_node()
	print("Objects node is: ", objects)

	arr_nm = client.get_namespace_array()
	print(arr_nm)

	list_obj = objects.get_children()
	print(list_obj)
	myobj = list_obj[1].get_children()
	print(myobj)

	opcevent = OPC_Event()
	sub = client.create_subscription(500,opcevent)
	handler1 = sub.subscribe_data_change(myobj[0])
	# handler2 = sub.subscribe_data_change(myobj[1])



if __name__ == "__main__":
	opc_test2()