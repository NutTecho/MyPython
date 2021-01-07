import snap7.client as c
# from snap7.snap7types import * 
# from snap7.util import *

plc = c.Client()
plc.connect('127.0.0.1',0,1)  
print(plc.connect)