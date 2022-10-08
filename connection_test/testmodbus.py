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

from pymodbus.datastore import (
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSparseDataBlock,
    ModbusSequentialDataBlock,
    ModbusSparseDataBlock
)

# from pymodbus.server.async_io import StartTcpServer

from pymodbus.server.sync import StartSerialServer
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from threading import Thread
import time

    
# plc = ModbusSerialClient(method='rtu',port='COM1',baudrate=9600)

store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        co = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        hr = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        ir = ModbusSequentialDataBlock(0x00, [0]*0x0F))

def run_server(host,port):
    context = ModbusServerContext(slaves=store, single=True)
    identity = ModbusDeviceIdentification()
    #      info = {
    #         "VendorName" = 'Pymodbus'
    #         "ProductCode" = 'PM'
    #         "VendorUrl" = 'http://github.com/riptideio/pymodbus/'
    #         "ProductName" = 'Pymodbus Server'
    #         "ModelName" = 'Pymodbus Server'
    #         "MajorMinorRevision" = '2.3.0',
    #     }
    # )
    # identity.VendorName = 'Pymodbus'
    # identity.ProductCode = 'PM'
    # identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    # identity.ProductName = 'Pymodbus Server'
    # identity.ModelName = 'Pymodbus Server'
    # identity.MajorMinorRevision = '2.3.0'

    print(f"Start Server Modbus at {host} : {port}")
    StartTcpServer(context, identity=identity,address=(host, port))

    
def update_server():
    i=0
    while (True):
        register = 3
        # address = 0x01
        store.setValues(register, 0x01, [i])
        store.setValues(register, 0x02, [123])
        print("sucsess")
        i += 1
        time.sleep(1)

if __name__ == "__main__":
  
    Thread(target=run_server,args=('192.168.11.10',502)).start()
    Thread(target=update_server).start()

