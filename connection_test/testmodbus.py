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

# plc = ModbusSerialClient(method='rtu',port='COM1',baudrate=9600)

def run_server(host,port):
    store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        co = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        hr = ModbusSequentialDataBlock(0x00, [0]*0x0F),
        ir = ModbusSequentialDataBlock(0x00, [0]*0x0F))

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
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '2.3.0'

    print(f"Start Server Modbus at {host} : {port}")
    StartTcpServer(context, identity=identity,address=(host, port))
    
# for i,d in enumerate(a):
#     xplc.write_register(i,d,unit=1)

if __name__ == "__main__":
    # xplc = ModbusTcpClient(host='127.0.0.1',port=502)
    # xplc.write_register(0,100,unit=0x02)
    # print(xplc.registers[0])
    run_server('127.0.0.1',502)