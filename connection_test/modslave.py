from pymodbus.client.sync import (
    ModbusSerialClient,
    ModbusTcpClient,
    ModbusTlsClient,
    ModbusUdpClient,
)
from pymodbus.transaction import (
    ModbusAsciiFramer,
    ModbusBinaryFramer,
    ModbusRtuFramer,
    ModbusSocketFramer,
    ModbusTlsFramer,
)
# from pymodbus.diag_message import * 
# from pymodbus.file_message import *
# from pymodbus.other_message import *
# from pymodbus.mei_message import *
# from pymodbus.repl.client import ModbusTcpClient
# import time
# client = ModbusTcpClient(host='192.168.10.29',port=502)
# a = client.report_slave_id()
# UNIT = 0x02

# client = ModbusSerialClient(method = 'rtu',port='COM1',baudrate=9600)
# rr = client.report_slave_id(unit = 1)
# print(rr)
# client.connect()
# a = client.read_coils(1,1,unit=2).bits[0]

# from easymodbus.modbusClient import ModbusClient
# client = ModbusClient('127.0.0.1',502)
# client.unitidentifier = 2
# client.connect()
# a = client.read_holdingregisters(1,1)
# client.write_single_register(3,300)
# client.close()
# print(a)

client = ModbusTcpClient(host='127.0.0.1',port=502,framer=ModbusSocketFramer)

def WriteData(slave_id,address,count,value):
    client.write_registers(address,[value]*count,unit = slave_id)

def ReadData(slave_id,address,count):
    x = client.read_holding_registers(address,count,unit = slave_id)
    print(x.registers)

def ReadCoil(slave_id,address,count):
    x = client.read_coils(address,count,unit=slave_id).bits
    print(x)

def WriteCoil(slave_id,address,count,value):
    if value == "ON":
        status = True
    else:
        status = False
    x = client.write_coils(address,[status]*count,unit = slave_id)
    # print(x)

def WriteString(slave_id,address,count,value):
    client.write_registers(address,[0]*count,unit=slave_id)
    if len(value)%2 > 0:
        value = value + " "
    c = len(value)//2
    for i in range(c):
        y = value[0 + (2*i):2 + (2*i)]
        print(y)
        q = [ hex(ord(r))[2:4] for r in y]
        print(q)
        k = int(q[0]+q[1],16)
        client.write_registers(address+i,k,unit=slave_id)



print(client.connect())
# WriteData(2,0,2,555)
# ReadData(3,0,8)
# ReadCoil(1,0,8)
WriteCoil(3,0,3,"ON")
# WriteString(client,0,8,"banana")




