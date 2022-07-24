from opcua import Client
import time


if __name__ == "__main__":

    client = Client("opc.tcp://172.23.32.1:4841/freeopcua/server/")
    
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        client.load_type_definitions()
        print("connect")
        #     # client.load_type_definitions
        #     # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        #     # Node objects have methods to read and write node attributes as well as browse or populate address space
        #     # print("Children of root are: ", root.get)

        #     # get a specific node knowing its node id
        #     #var = client.get_node(ua.NodeId(1002, 2))
        # var = client.get_node("ns=2;i=2")
        # print(var)
        #     #var.get_data_value() # get value of node as a DataValue object
        #     #var.get_value() # get value of node as a python builtin
        #     #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #     #var.set_value(3.9) # set node value using implicit data type

        uri = "http://examples.freeopcua.github.io"
        idx = client.get_namespace_index(uri)

        #     # Now getting a variable node using its browse path
        myvar = root.get_child(["0:Objects", "{}:MyObject".format(idx), "{}:MyVariable".format(idx)])
        obj = root.get_child(["0:Objects", "{}:MyObject".format(idx)])
        print("myvar is: ", myvar)

        # #     # Stacked myvar access
        # #     # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].get_value())
        while True:
            time.sleep(1)
            print(myvar.get_value())
    finally:
        pass
    # #     # client.disconnect()