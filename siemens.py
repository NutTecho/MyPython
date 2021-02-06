
import snap7.client as c
from snap7.snap7types import *
from snap7.util import *
from datetime import datetime

def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype == S7WLBit:
        return get_bool(result,0,1)
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

plc = c.Client()
plc.connect('192.168.137.1',0,1,102)  
if plc.get_connected():
    print("connect sucsess")
else:
    print("connect fail")

# cpu = plc.get_cpu_info()
# print(cpu)
x = ReadMemory(plc,10,0,S7WLWord)
print(x)
WriteMemory(plc,20,0,S7WLWord,245)

