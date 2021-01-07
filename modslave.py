# from pymodbus.client.sync import ModbusTcpClient
# from pymodbus.client.sync import ModbusSerialClient
# from pymodbus.server.sync import ModbusTcpServer
# from pymodbus.diag_message import * 
# from pymodbus.file_message import *
# from pymodbus.other_message import *
# from pymodbus.mei_message import *
from pymodbus.repl.client import ModbusTcpClient
# import time
client = ModbusTcpClient(host='192.168.10.29',port=502)
# a = client.report_slave_id()
# UNIT = 0x02
a = client.read_holding_registers(address=1,count= 1,unit = 10)
client.write_registers(1,[100]*8,unit=2)
print(a)

# client = ModbusSerialClient(method = 'rtu',port='COM1',baudrate=9600)
# rr = client.report_slave_id(unit = 1)
# print(rr)
# client.connect()
# a = client.read_coils(1,1,unit=2).bits[0]

# b1 = client.read_holding_registers(1,1,unit=1).registers[0]
# rq = r(unit = 1)
# rr = client.execute(
# print(rr)
# time.sleep(1)
# b2 = client.read_holding_registers(1,1,unit=2).registers[0]
# print(a)
# print(b1)
# print(b2)
# from easymodbus.modbusClient import ModbusClient
# client = ModbusClient('127.0.0.1',502)
# client.unitidentifier = 2
# client.connect()
# a = client.read_holdingregisters(1,1)
# client.write_single_register(3,300)
# client.close()
# print(a)
