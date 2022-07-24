import snap7
from snap7.types import *
from snap7.util import *
from datetime import datetime
import struct

# Area table in snap7
# area        value        mean
# S7AreaPE      0x81    Process Input
# S7AreaPA      0x82    Process Output
# S7AreaMK      0x83    Markers
# S7AreaDB      0x84    DB
# S7AreaCT      0x1C    Counters
# S7AreaTM      0x1D    Timers

# word len in snap 7
# type      value      mean
# S7WLBit     0X01    Bit(inside word)
# S7WLByte    0X02    Byte(8 bit)
# S7WLWord    0X04    Word(16 bit)
# S7WLDWord   0X06    Double Word(32 bit)
# S7WLReal    0X08    Real (32 bit float)
# S7WLCounter 0X1C    Counter(16 bit)
# S7WLTimer   0X1D    Timer (16 bit)


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype == S7WLBit:
        return get_bool(result,0,bit)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return get_int(result,0)
    elif datatype == S7WLReal:
        return get_real(result,0)
    elif datatype == S7WLDWord:
        return get_dword(result,0)

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype == S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype == S7WLByte or datatype == S7WLWord:
        set_int(result,0,value)
    elif datatype == S7WLReal:
        set_real(result,0,value)
    elif datatype == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['MK'],0,byte,result)
    print(f"Write Memory MW{byte} sucsess")

def WriteInput(plc,byte,bit,value):
    result = plc.read_area(areas['PE'],0,byte,S7WLBit)
    set_bool(result,0,bit,value)
    plc.write_area(areas['PE'],0,byte,result)
    print("write sucsess")


def ReadInput(plc,dbnum,byte):
    result = plc.read_area(areas['PE'],dbnum,byte,S7WLBit)
    return get_bool(result,0,0)
    
def ReadOutput(plc,dbnum,byte):
    result = plc.read_area(areas['PA'],dbnum,byte,S7WLBit)
    return get_bool(result,0,0)

def ReadDB(plc,dbnum,byte,bit,datatype):
    result = plc.read_area(areas['DB'],dbnum,byte,datatype)
    if datatype == S7WLBit:
        return get_bool(result,0,bit)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return result
    elif datatype == S7WLReal:
        return get_real(result,0)
    elif datatype == S7WLDWord:
        return get_dword(result,0)


def WriteDB(plc,dbnum,byte,bit,datatype,value):
    result = plc.read_area(areas['DB'],dbnum,byte,datatype)
    if datatype == S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype == S7WLByte or datatype == S7WLWord:
        set_int(result,0,value)
    elif datatype == S7WLReal:
        set_real(result,0,value)
    elif datatype == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['DB'],dbnum,byte,result)
    print("write sucsess")

plc = snap7.client.Client()
plc.connect("127.0.0.1",0,1,102)  
if plc.get_connected():
    print("connect sucsess")
else:
    print("connect fail")

# buffer = plc.db_get(2)
# print(buffer)
block_info = plc.get_cpu_state()
print(block_info)

# dt = plc.get_plc_datetime()()
# print(dt)

readx = plc.db_read(2,0,6)
print(bytes(readx))
print(int.from_bytes(bytes(readx),"big"))
print(struct.unpack('h'*3,bytes(readx)))
print(readx.decode())
# cpu = plc.get_cpu_info()
# print(cpu)
# print(S7WLReal)

# x = ReadMemory(plc,38,0,S7WLDWord)
# q = struct.unpack('!L', x)[0]
# print(q)

# x = ReadDB(plc,2,0,0,S7WLWord)
# print(x)
# for i in range(6):
#     x = ReadDB(plc,1,22 + i,0,S7WLWord)
#     print(x)

# x = ReadDB(plc,1,27,0,S7WLByte)
# print(x)
# print(struct.unpack('BB',x))
# print(get_int(x,0))
# print(struct.unpack('h',x)[0])
# arr = bytearray([13,0])
# print(arr)
# print(struct.unpack('BB',arr)[0])

# print(struct.calcsize('!BB'))

# z = ReadDB(plc,1,25,0,S7WLByte)
# print(struct.pack('h',z))

# y = ReadDB(plc,1,26,0,S7WLByte)
# print(struct.pack('h',y))

# a = ReadDB(plc,1,28,0,S7WLByte)
# a1 = struct.pack('hh',a)
# print(struct.unpack('i',a1))


# struct.unpack("HH",x)

# WriteMemory(plc,300,0,S7WLWord,245)
# WriteInput(plc,1,1,1)
# WriteDB(plc,6,0,0,S7WLWord,12)

# y = ReadOutput(plc,0,4)
# print(y)
# for j in range(0,8):                    
#     if (int(struct.unpack('!B', y)[0]) & pow(2,j)!=0):
#         i_temp_value=1
#     else:
#         i_temp_value=0
#     print(i_temp_value)

