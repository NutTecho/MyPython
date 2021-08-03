from opcua import Server
from random import randint
import datetime
import time

serv = Server()
url = "opc.tcp://127.0.0.1:4840"
serv.set_endpoint(url)

name = "OPC_SIMULATION_SERVER"
addspace = serv.register_namespace(name)

node = serv.get_objects_node()
param = node.add_object(addspace,"Parameters")

Temp = param.add_variable(addspace,"Temperature",0)
Press = param.add_variable(addspace,"Pressure",0)
Time = param.add_variable(addspace,"Time",0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

serv.start
print("server start at {}".format(url))

while(True):
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    nTime = datetime.datetime.now()

    print(Temperature,Pressure,nTime)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(nTime)

    time.sleep(2)