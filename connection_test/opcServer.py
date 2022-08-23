from opcua import Server
from random import randint
import datetime
import time

def test_opc1():
    server = Server()
    uri = "opc.tcp://localhost:4843"
    # server.set_server_name("demo_serv")
    server.set_endpoint(uri)

    name = "demo"
    addspace = server.register_namespace(name)

    node = server.get_objects_node()
    print(node)

    # param = node.add_object(addspace,"Parameters")
    param = node.add_object(addspace,"MyObject")
    # Temp = param.add_variable(addspace,"Myvar",0.0)
    # Temp.set_writable()

    Temp = param.add_variable(addspace,"Temperature",0.0)
    Press = param.add_variable(addspace,"Pressure",0.0)
    Time = param.add_variable(addspace,"Time",0.0)

    Temp.set_writable()
    Press.set_writable()
    Time.set_writable()

    server.start()

    print("server start at {}".format(uri))

    try:
        while(True):
            Temperature = float(randint(10,50))
            Pressure = float(randint(200,999))
            nTime = datetime.datetime.now()

            print(Temperature)

            Temp.set_value(Temperature)
            Press.set_value(Pressure)
            Time.set_value(nTime)

            time.sleep(2)
    finally:
        pass

def test_opc2():
    server = Server()
    uri = "opc.tcp://172.29.48.1:4843"
    server.set_endpoint(uri)
    server.import_xml("opc_conf1.xml")
    

    objects = server.get_objects_node()
    list_obj = objects.get_children()
    myobj = list_obj[1].get_children()
    print(myobj)

  
    myobj[0].set_writable()
    myobj[1].set_writable()

    # list_var = [item.set_writable() for item in myobj]
    # print(list_var)

    server.start()

    try:
        while(True):

            Humid = float(randint(10,50))
            Temp = float(randint(200,999))

            myobj[0].set_value(Humid)
            myobj[1].set_value(Temp)

            time.sleep(2)
    finally:
        pass



if __name__ == "__main__":
#    test_opc1()
   test_opc2()