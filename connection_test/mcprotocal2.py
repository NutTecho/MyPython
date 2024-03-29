import pymcprotocol
import struct

#If you use Q series PLC
# pymc3e = pymcprotocol.Type3E()
#if you use L series PLC,
# pymc3e = pymcprotocol.Type3E(plctype="L")
#if you use QnA series PLC,
# pymc3e = pymcprotocol.Type3E(plctype="QnA")
#if you use iQ-L series PLC,
# pymc3e = pymcprotocol.Type3E(plctype="iQ-L")
#if you use iQ-R series PLC,
# pymc3e = pymcprotocol.Type3E(plctype="iQ-R")

#If you use 4E type
# pymc4e = pymcprotocol.Type4E()

#If you use ascii byte communication, (Default is "binary")
# pymc3e.setaccessopt(commtype="binary")
# pymc3e.connect("192.168.3.39", 2000)


#======= Send command================
#read from D100 to D110
# wordunits_values = pymc3e.batchread_wordunits(headdevice="D100", readsize=10)

#read from X10 to X20
# bitunits_values = pymc3e.batchread_bitunits(headdevice="X10", readsize=10)

#write from D10 to D15
# pymc3e.batchwrite_wordunits(headdevice="D10", values=[0, 10, 20, 30, 40])

#write from Y10 to Y15
# pymc3e.batchwrite_bitunits(headdevice="Y10", values=[0, 1, 0, 1, 0])

#read "D1000", "D2000" and  dword "D3000".
# word_values, dword_values = pymc3e.randomread(word_devices=["D1000", "D2000"], dword_devices=["D3000"])

#write 1000 to "D1000", 2000 to "D2000" and 655362 todword "D3000"
# pymc3e.randomwrite(word_devices=["D1000", "D1002"], word_value=[1000, 2000], 
                #    dword_devices=["D1004"], dword_values=[655362])

#write 1(ON) to "X0", 0(OFF) to "X10"
# pymc3e.randomwrite_bitunits(bit_devices=["X0", "X10"], values=[1, 0])



#============ Remote Operation===============
#remote run, clear all device
# pymc3e.remote_run(clear_mode=2, force_exec=True)

#remote stop
# pymc3e.remote_stop()

#remote latch clear. (have to PLC be stopped)
# pymc3e.remote_latchclear()

#remote pause
# pymc3e.remote_pause(force_exec=False)

#remote reset
# pymc3e.remote_reset()

#read PLC type
# cpu_type, cpu_code = pymc3e.read_cputype()
# print(cpu_type,cpu_code)

#Unlock PLC,
#If you set PLC to locked, you need to unlkock to remote operation
#Except iQ-R, password is 4 character.
# pymc3e.remote_unlock(password="1234")
#If you want to hide password from program
#You can enter passwrod directly
# pymc3e.remote_unlock(request_input=True)

#Lock PLC
# pymc3e.remote_lock(password="1234")
# pymc3e.remote_lock(request_input=True)


# ///////////////////////////////////////////////////
def main():
    pymc3e = pymcprotocol.Type3E()
    pymc3e.setaccessopt(commtype="binary",timer_sec=10)
    pymc3e.connect(ip="192.168.3.39",port=1026)
    if pymc3e._is_connected:
        cpu_type, cpu_code = pymc3e.read_cputype()
        print(cpu_type,cpu_code)

    def readsting(head,size):
        sumdata = ""
        getdata = pymc3e.batchread_wordunits(headdevice=head, readsize=size)
        convert = list(map(lambda x : (struct.pack('H',x)).decode("UTF-8")  , getdata))
        for r in convert :
            sumdata += r
        return sumdata

    def readword(head):
        getdata = pymc3e.batchread_wordunits(headdevice=head, readsize=1)
        return getdata

    def readarray(head,size):
        getdata = pymc3e.batchread_wordunits(headdevice=head, readsize=size)
        return getdata

    a = readword("D100")
    # b =  readsting("D200",10)
    print(a)


if __name__ == "__main__":
    main()