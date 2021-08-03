from pymodbus.client.sync import ModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.server.sync import StartSerialServer
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusServerContext,ModbusSlaveContext
from pymodbus.datastore import ModbusSequentialDataBlock,ModbusSparseDataBlock
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
plc = ModbusSerialClient(method='rtu',port='COM1',baudrate=9600)

def run_server():
    store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0, [17]*100),
        co = ModbusSequentialDataBlock(0, [17]*100),
        hr = ModbusSequentialDataBlock(0, [17]*100),
        ir = ModbusSequentialDataBlock(0, [17]*100))

    context = ModbusServerContext(slaves=store, single=True)
    
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '2.3.0'

    StartTcpServer(context, identity=identity,address=('127.0.0.1', 502))

# for i,d in enumerate(a):
#     xplc.write_register(i,d,unit=1)

if __name__ == "__main__":
    # xplc = ModbusTcpClient(host='127.0.0.1',port=502)
    # xplc.write_register(0,100,unit=0x02)
    # print(xplc.registers[0])
    run_server()