from opcua import Server , ua
import time


if __name__ == "__main__":

    # setup our server
    server = Server()
    uri = "opc.tcp://172.28.192.1:4843"
    server.set_endpoint(uri)

    # server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
    # server.set_security_IDs(["Basic256Sha256"])
    # server.load_certificate("certificate.pem")
    # server.load_private_key("key.pem")

    # setup our own namespace, not really necessary but should as spec
    # server.set_server_name("FreeOpcUa Example Server")
    # url = "http://examples.freeopcua.github.io"
    # idx = server.register_namespace(url)
    name = "demo"
    name2 = "demo2"
    idx = server.register_namespace(name)
    idx2 = server.register_namespace(name2)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    tempdata = myobj.add_variable(idx, "Temp", 0.0)
    leveldata = myobj.add_variable(idx, "Level", 0.0)
    tempdata.set_writable()    # Set MyVariable to be writable by clients
    leveldata.set_writable()

    myobj2 = objects.add_object(idx2, "MyObject2")
    myvar2 = myobj2.add_variable(idx2, "MyVariable2", 12.34)

    # starting!
    server.start()
    # idx.set_attribute_value(2,10.5)
    
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 1
            if count == 100 :
                count = 0
            tempdata.set_value(count)
            leveldata.set_value(count + 5.0)
            print(count)
    finally:
        # pass
        #close connection, remove subcsriptions, etc
        server.stop()