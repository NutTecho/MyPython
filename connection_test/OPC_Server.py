from opcua import Server , ua
import time


if __name__ == "__main__":

    # setup our server
    server = Server()
    uri = "opc.tcp://localhost:4843"
    server.set_endpoint(uri)

    # server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
    # server.set_security_IDs(["Basic256Sha256"])
    server.load_certificate("certificate.pem")
    server.load_private_key("key.pem")

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
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

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
            myvar.set_value(count)
            print(count)
    finally:
        # pass
        #close connection, remove subcsriptions, etc
        server.stop()