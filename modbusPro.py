from pickle import *
from tkinter import *
from tkinter import ttk
from datetime import datetime
from pymodbus.client.sync import ModbusSerialClient, ModbusTcpClient
from threading import Thread
from time import sleep, perf_counter
import struct
import serial
import requests

class LINE:
    def __init__(self, token):
        self.url = 'https://notify-api.line.me/api/notify'
        self.LINE_HEADERS = {'Authorization': 'Bearer ' + token}
        self.session = requests.Session()

    def sendtext(self, msg):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={"message": msg})
        return response.text


class Message1:
    def __init__(self, root, title, row, column, var, var2, var3):
        self.root = root
        self.title = title
        self.row  = row
        self.column = column
        self.var = var
        self.var2 = var2
        self.var3 = var3

        F = LabelFrame(self.root, text = self.title)
        F.grid(row = self.row, column = self.column, padx = 5, pady = 5, ipadx = 5, ipady = 2, sticky = "news")
        ttk.Radiobutton(F, text="Disable", value=False, variable = self.var).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "sw")
        ttk.Radiobutton(F, text="Enable", value=True, variable = self.var).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "sw")
        ttk.Label(F, text = "Address  ").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var2 , width = 14).grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")
        ttk.Label(F, text = "Message").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var3 , width = 14).grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")


class Message2:
    def __init__(self, root, title, row, column, var, var2, var3, var4, var5):
        self.root = root
        self.title = title
        self.row  = row
        self.column = column
        self.var = var
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5

        F = LabelFrame(self.root, text = self.title)
        F.grid(row = self.row, column = self.column, padx = 5, pady = 5, ipadx = 5, ipady = 2, sticky = "news")
        ttk.Radiobutton(F, text="Disable", value=False, variable = self.var).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "sw")
        ttk.Radiobutton(F, text="Enable", value=True, variable = self.var).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "sw")
        ttk.Label(F, text = "Address Trig").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var2 , width = 10).grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")
        ttk.Label(F, text = "Address Data ").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var3 , width = 10).grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")
        ttk.Label(F, text = "Message").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var4 , width = 10).grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "w")
        ttk.Label(F, text = "Unit").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        ttk.Entry(F, textvariable = self.var5 , width = 10).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "w")

class Message2_T:
    def __init__(self, root, title, row, column, var):
        self.root = root
        self.title = title
        self.row  = row
        self.column = column
        self.var = var

        F = LabelFrame(self.root, text = self.title)
        F.grid(row = self.row, column = self.column, padx = 5, pady = 5, ipadx = 5, ipady = 2, sticky = "news")
        ttk.Radiobutton(F, text="Int16", value=0, variable = self.var).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "sw")
        ttk.Radiobutton(F, text="Int32", value=1, variable = self.var).grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "sw")
        ttk.Radiobutton(F, text="Float32", value=2, variable = self.var).grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "sw")


stop_thread = True
connected = False

msgs1_enable_list = [] 
msgs1_address_list = []
msgs1_message_list = []
msgs2_enable_list = [] 
msgs2_address_trig_list = []
msgs2_address_data_list = []
msgs2_message_list = []
msgs2_unit_list = []
msgs2_type_list = []


def convertToInt32(l, h):
    raw = struct.pack('>HH', l, h)
    return struct.unpack('>i', raw)[0]


def convertToFloat32(l, h):
    raw = struct.pack('>HH', l, h)
    return round(struct.unpack('>f', raw)[0], 2)

def _destroy():  
    if stop_thread == True and connected == False:
        root.destroy() 


def _insertText(text):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    T.configure(state = "normal")
    T.insert(END, f" {dt}\n  -{text}\n\n")
    T.configure(state = "disable")


def _clear_text():
    T.configure(state = "normal")
    T.delete("1.0", END)
    T.configure(state = "disable")


def _connect():
    global commu_mode
    global config
    global tcp_ip, tcp_port, tcp_slave_id  
    global rtu_com_port, rtu_slave_id, rtu_buadrate, rtu_parity, rtu_stopbit
    global token
    global connected
    global stop_thread
    global db
    global T_tcp
    global T_rtu
    global msg
    global msgs1_state
    global msgs2_state
    if connected == False: 
        try:
            msgs1_enable_list.clear() 
            msgs1_address_list.clear()
            msgs1_message_list.clear()
            msgs2_enable_list.clear() 
            msgs2_address_trig_list.clear()
            msgs2_address_data_list.clear()
            msgs2_message_list.clear()
            msgs2_unit_list.clear()
            msgs2_type_list.clear()

            commu_mode = c_mode.get()
            # ----------TCP---------------------------------------
            tcp_ip = tcp_ip_address.get()
            tcp_port = tcp_c_port.get()
            tcp_slave_id = tcp_config_id.get()
            # ----------TCP---------------------------------------
            
            # ----------RTU---------------------------------------
            rtu_com_port = rtu_c_com_port.get()
            rtu_slave_id = rtu_config_id.get()
            rtu_buadrate = rtu_config_baudrate.get() 
            # ----------Parity------------------------------------
            if list_parity.get() == "Even Parity":
                rtu_parity = serial.PARITY_EVEN
            elif list_parity.get() == "Odd Parity":
                rtu_parity = serial.PARITY_ODD
            else:
                rtu_parity = serial.PARITY_NONE
            # ----------Parity------------------------------------
            # ----------Stopbit-----------------------------------        
            if list_stop_bit.get() == "1 Stop bit":
                rtu_stopbit = serial.STOPBITS_ONE
            else:
                rtu_stopbit = serial.STOPBITS_TWO
            # ----------Stopbit-----------------------------------
            # ----------RTU---------------------------------------
            token = line_token.get()
            # ----------Enable-------------------------------------------------------
            for i in range(12):
                msgs1_enable_list.append(msgs1_enable[i].get())
                msgs1_address_list.append(msgs1_addr[i].get())
                msgs1_message_list.append(msgs1_msg[i].get())
            for j in range(12):
                msgs2_enable_list.append(msgs2_enable[j].get())
                msgs2_address_trig_list.append(msgs2_addr_trig[j].get())
                msgs2_address_data_list.append(msgs2_addr_data[j].get())
                msgs2_message_list.append(msgs2_msg[j].get())
                msgs2_unit_list.append(msgs2_unit[j].get())
                msgs2_type_list.append(msgs2_t[j].get())
            # ----------Enable-------------------------------------------------------
            msgs1_state = [False] * 12
            msgs2_state = [False] * 12
            msg = LINE(token)
        except Exception as e:     
            _insertText(e)   
        else:
            stop_thread = False  
            connected = True 
            if commu_mode == False:
                T_tcp = Thread(target=_tcp)
                T_tcp.start()
                _insertText("TCP Connected")
            else:
                T_rtu = Thread(target=_rtu)
                T_rtu.start()
                _insertText("RTU Connected")


def _disconnect():
    global connected
    global stop_thread
    if connected == True:
        try:
            stop_thread = True
            sleep(1.5)
            if commu_mode == False:
                clientTCP.close()
            else:
                clientRTU.close()
        except Exception as e:
            _insertText(e)
        else:
            connected = False         


def _tcp():
    global clientTCP
    global T_tcp
    prevTime = 0.00
    cl_state = False
    cl = working_status.cget('bg')
    try:
        clientTCP = ModbusTcpClient(tcp_ip, tcp_port)        
        clientTCP.connect()
        sleep(1)
        while True:
            result_msg1 = [False] * 12
            result_msg2_bit = [False] * 12
            result_msg2_register = [0] * 12
            for i in range(12):
                if msgs1_enable_list[i] == True:
                    result_msg1[i] = clientTCP.read_coils(msgs1_address_list[i], 1, unit = tcp_slave_id).bits[0]
            for j in range(12):
                if msgs2_enable_list[j] == True:
                    result_msg2_bit[j] = clientTCP.read_coils(msgs2_address_trig_list[j], 1, unit = tcp_slave_id).bits[0]
                    if msgs2_type_list[j] == 0:
                        result_msg2_register[j] = clientTCP.read_holding_registers(msgs2_address_data_list[j]-40000, 1, unit = tcp_slave_id).registers[0]
                    elif msgs2_type_list[j] == 1:
                        temp1, temp2 = clientTCP.read_holding_registers(msgs2_address_data_list[j]-40000, 2, unit = tcp_slave_id).registers[::]
                        result_msg2_register[j] = convertToInt32(temp1, temp2)
                    else:
                        temp1, temp2 = clientTCP.read_holding_registers(msgs2_address_data_list[j]-40000, 2, unit = tcp_slave_id).registers[::]
                        result_msg2_register[j] = convertToFloat32(temp1, temp2)

            for ii in range(12):
                if result_msg1[ii] == True and msgs1_state[ii] == False:
                    msg.sendtext(msgs1_message_list[ii])
                    _insertText(f"Message.{ii+1}  {msgs1_message_list[ii]}")
                    msgs1_state[ii] = True
                if result_msg1[ii] == False and msgs1_state[ii] == True:
                    msgs1_state[ii] = False
                if stop_thread == True:
                    break
            for jj in range(12):
                if result_msg2_bit[jj] == True and msgs2_state[jj] == False:
                    msg.sendtext(f"{msgs2_message_list[jj]} {result_msg2_register[jj]} {msgs2_unit_list[jj]}")
                    _insertText(f"Message.{jj+13}  {msgs2_message_list[jj]} {result_msg2_register[jj]} {msgs2_unit_list[jj]}")
                    msgs2_state[jj] = True
                if result_msg2_bit[jj] == False and msgs2_state[jj] == True:
                    msgs2_state[jj] = False
                if stop_thread == True:
                    break
            
            currentTime = perf_counter()
            if round(currentTime - prevTime, 2) > .50:
                prevTime = currentTime
                cl_state = (not cl_state)
                if cl_state == True:
                    cl = 'green'
                else:
                    cl = 'white'
                working_status.config(bg= cl)

            if stop_thread == True:
                break            
    except Exception as e:
        _insertText(e)
    else:
        _insertText("TCP Disconnected")
        working_status.config(bg= 'white')


def _rtu():
    global clientRTU
    global T_rtu
    prevTime = 0.00
    cl_state = False
    cl = working_status.cget('bg')
    try:
        clientRTU = ModbusSerialClient('rtu')     
        clientRTU.port = rtu_com_port        
        clientRTU.baudrate = rtu_buadrate
        clientRTU.parity = rtu_parity
        clientRTU.stopbits = rtu_stopbit
        clientRTU.connect()      
        sleep(1)
        while True:
            result_msg1 = [False] * 12
            result_msg2_bit = [False] * 12
            result_msg2_register = [0] * 12
            for i in range(12):
                if msgs1_enable_list[i] == True:
                    result_msg1[i] = clientRTU.read_coils(msgs1_address_list[i], 1, unit = rtu_slave_id).bits[0]
            for j in range(12):
                if msgs2_enable_list[j] == True:
                    result_msg2_bit[j] = clientRTU.read_coils(msgs2_address_trig_list[j], 1, unit = rtu_slave_id).bits[0]
                    if msgs2_type_list[j] == 0:
                        result_msg2_register[j] = clientRTU.read_holding_registers(msgs2_address_data_list[j]-40000, 1, unit = rtu_slave_id).registers[0]
                    elif msgs2_type_list[j] == 1:
                        temp1, temp2 = clientRTU.read_holding_registers(msgs2_address_data_list[j]-40000, 2, unit = rtu_slave_id).registers[::]
                        result_msg2_register[j] = convertToInt32(temp1, temp2)
                    else:
                        temp1, temp2 = clientRTU.read_holding_registers(msgs2_address_data_list[j]-40000, 2, unit = rtu_slave_id).registers[::]
                        result_msg2_register[j] = convertToFloat32(temp1, temp2)
            for ii in range(12):
                if result_msg1[ii] == True and msgs1_state[ii] == False:
                    msg.sendtext(msgs1_message_list[ii])
                    _insertText(f"Message.{ii+1}  {msgs1_message_list[ii]}")
                    msgs1_state[ii] = True
                if result_msg1[ii] == False and msgs1_state[ii] == True:
                    msgs1_state[ii] = False
                if stop_thread == True:
                    break
            for jj in range(12):
                if result_msg2_bit[jj] == True and msgs2_state[jj] == False:
                    msg.sendtext(f"{msgs2_message_list[jj]} {result_msg2_register[jj]} {msgs2_unit_list[jj]}")
                    _insertText(f"Message.{jj+13}  {msgs2_message_list[jj]} {result_msg2_register[jj]} {msgs2_unit_list[jj]}")
                    msgs2_state[jj] = True
                if result_msg2_bit[jj] == False and msgs2_state[jj] == True:
                    msgs2_state[jj] = False
                if stop_thread == True:
                    break
            
            currentTime = perf_counter()
            if round(currentTime - prevTime, 2) > .50:
                prevTime = currentTime
                cl_state = (not cl_state)
                if cl_state == True:
                    cl = 'green'
                else:
                    cl = 'white'
                working_status.config(bg= cl)

            if stop_thread == True:
                break 
                           
    except Exception as e:
        _insertText(e)
    else:
        _insertText("RTU Disconnected") 
        working_status.config(bg= 'white')       


def _save():
    data = [tcp_ip_address, tcp_c_port, tcp_config_id, rtu_c_com_port, rtu_config_id, rtu_config_baudrate, list_parity, list_stop_bit, line_token, c_mode]
    data2 = [msgs1_enable, msgs1_addr, msgs1_msg]
    data3 = [msgs2_enable, msgs2_addr_trig, msgs2_addr_data, msgs2_msg, msgs2_unit, msgs2_t]
    try:
        with open("datasaved.dat", "wb") as pickle_file:
            for save in data:
                dump(save.get(), pickle_file, HIGHEST_PROTOCOL)
            
            for save2 in data2:
                for save2_1 in range(12):
                    dump(save2[save2_1].get(), pickle_file, HIGHEST_PROTOCOL)
            
            for save3 in data3:
                for save3_2 in range(12):
                    dump(save3[save3_2].get(), pickle_file, HIGHEST_PROTOCOL)
    except Exception as e:
        _insertText(e)
    else:
        _insertText("Configuration was saved")


def _load():
    data = [tcp_ip_address, tcp_c_port, tcp_config_id, rtu_c_com_port, rtu_config_id, rtu_config_baudrate, list_parity, list_stop_bit, line_token, c_mode]
    data2 = [msgs1_enable, msgs1_addr, msgs1_msg]
    data3 = [msgs2_enable, msgs2_addr_trig, msgs2_addr_data, msgs2_msg, msgs2_unit, msgs2_t]
    try:
        with open("datasaved.dat", "rb") as pickle_file:
            for d_load in data:
                d_load.set(load(pickle_file))
            
            for d_load2 in data2:
                for d_load2_2 in range(12):
                    d_load2[d_load2_2].set(load(pickle_file))   

            for d_load3 in data3:
                for d_load3_2 in range(12):
                    d_load3[d_load3_2].set(load(pickle_file))
    except Exception as e:
        _insertText(e)
    else:
        _insertText("Configuration was loaded")


root = Tk()
# -------------Setting header--------------------
root.title("Line Notify")
root.geometry("750x580")
root.option_add("*Font", "Arial 13")
root.resizable(0, 0)
# -------------Setting header--------------------

# -------------Notebooks-------------------------
tab = ttk.Notebook(root)
config = Frame(tab)
page1 = Frame(tab)
page2 = Frame(tab)
page3 = Frame(tab)
tab.add(config, text = "Configuration")
tab.add(page1, text = "Messages 1")
tab.add(page2, text = "Messages 2")
tab.add(page3, text = "Messages 3")
tab.pack(fill = BOTH, expand = 1)
# -------------Notebooks------------------------

c_mode = BooleanVar()
# -------------Modbus TCP---------------------------------------------------------------------------------------------------------------------
tcp_ip_address = StringVar()
tcp_c_port = IntVar()
tcp_config_id = IntVar()

F1 = LabelFrame(config, text = "TCP Configuration")
F1.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5, sticky = "news")

ttk.Radiobutton(F1, text="TCP", value=False, variable=c_mode).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "sw")

ttk.Label(F1, text = "IP Address  ").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F1, textvariable = tcp_ip_address, justify = "left", width = 15).grid(row = 1, column = 1, padx = 0, pady = 5, sticky = "sw")

ttk.Label(F1, text = "Port").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F1, textvariable = tcp_c_port, justify = "left", width = 15).grid(row = 2, column = 1, padx = 0, pady = 5, sticky = "sw")

ttk.Label(F1, text = "Slave ID").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F1, textvariable = tcp_config_id, justify = "left", width = 15).grid(row = 3, column = 1, padx = 0, pady = 5, sticky = "sw")
# -------------Modbus TCP---------------------------------------------------------------------------------------------------------------------

# -------------Modbus RTU---------------------------------------------------------------------------------------------------------------------
rtu_c_com_port = StringVar()
rtu_config_id = IntVar()
rtu_config_baudrate = IntVar()

F2 = LabelFrame(config, text = "RTU Configuration")
F2.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5, sticky = "news")

ttk.Radiobutton(F2, text="RTU", value=True, variable=c_mode).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "sw")

ttk.Label(F2, text = "Com Port").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F2, textvariable = rtu_c_com_port, justify = "left", width = 15).grid(row = 1, column = 1, padx = 0, pady = 5, sticky = "sw")

ttk.Label(F2, text = "Slave ID").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F2, textvariable = rtu_config_id, justify = "left", width = 15).grid(row = 2, column = 1, padx = 0, pady = 5, sticky = "sw")

ttk.Label(F2, text = "Baudrate     ").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(F2, textvariable = rtu_config_baudrate, justify = "left", width = 15).grid(row = 3, column = 1, padx = 0, pady = 5, sticky = "sw")

ttk.Label(F2, text = "Parity").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "sw")
list_parity = list_stop_bit = ttk.Combobox(F2, value = ["None Parity", "Odd Parity", "Even Parity"], width = 13, state = "readonly")
list_parity.grid(row = 4, column = 1, padx = 0, pady = 5, sticky = "swe")

ttk.Label(F2, text = "Stop Bit").grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "sw")
list_stop_bit = ttk.Combobox(F2, value = ["1 Stop bit", "2 Stop bits"], width = 13, state = "readonly")
list_stop_bit.grid(row = 5, column = 1, padx = 0, pady = 5, sticky = "swe")
# -------------Modbus RTU---------------------------------------------------------------------------------------------------------------------

line_token = StringVar()
L = LabelFrame(config, text = "Line Configuration")
L.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5, sticky = "news")
ttk.Label(L, text = "Line Token  ").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "sw")
ttk.Entry(L, textvariable = line_token, justify = "left", width = 15, show="X").grid(row = 0, column = 1, padx = 0, pady = 5, sticky = "se")

# -------------Status Message-----------------------------------------------------------------------------------------------
F3 = LabelFrame(config, text = "Status Message")
F3.grid(row = 0, column = 1, rowspan = 3, padx = 5, pady = 5, ipadx = 5, ipady = 5, sticky = "news")

T = Text(F3, height = 20, width = 47, font = "Consolas 12", wrap = "none")
T.grid(row = 0, column = 0, padx = 5, pady = 5)
T.configure(state = "disable")

Sx = Scrollbar(F3, orient = HORIZONTAL)
Sy = Scrollbar(F3)

Sx.grid(row = 1, column = 0, padx = 5, sticky = "we")
Sx.config(command = T.xview)
Sy.grid(row = 0, column = 1, pady = 5, sticky = "ns")
Sy.config(command = T.yview)

clear_messages_btn = ttk.Button(F3, text = "Clear", command = _clear_text)
clear_messages_btn.grid(row = 2, column = 0, pady = 10, ipadx = 2, ipady = 2, sticky = "se")
# -------------Status Message-----------------------------------------------------------------------------------------------

# -------------Control---------------------------------------------------------------------------------------------------------------------
working_status = Button(config, state="disabled", bg='white', font = "Consolas 9", width=10, relief="ridge", borderwidth = 2)
working_status.place(x=5, y=515, width=260, height=30)

btn_save_config = ttk.Button(config, text = "Save Config", command = _save)
btn_save_config.place(x=274, y=515, width=90, height=30)

btn_load_config = ttk.Button(config, text = "Load Config", command = _load)
btn_load_config.place(x=399, y=515, width=90, height=30)

btn_connect = ttk.Button(config, text = "Connect", command = _connect)
btn_connect.place(x=528, y=515, width=90, height=30)

btn_disconnect = ttk.Button(config, text = "Disconnect", command = _disconnect)
btn_disconnect.place(x=653, y=515, width=90, height=30)
# -------------Control---------------------------------------------------------------------------------------------------------------------

msgs1_enable, msgs1_addr, msgs1_msg, msgs2_enable, msgs2_addr_trig, msgs2_addr_data, msgs2_msg, msgs2_unit, msgs2_t = [], [], [], [], [], [], [], [], []
for i in range(12):
    msgs1_enable.append(str(i));  msgs1_addr.append(str(i)); msgs1_msg.append(str(i)); msgs2_enable.append(str(i)); msgs2_addr_trig.append(str(i))
    msgs2_addr_data.append(str(i)); msgs2_msg.append(str(i)); msgs2_unit.append(str(i)); msgs2_t.append(str(i))
    msgs1_enable[i] = BooleanVar(); msgs1_addr[i] = IntVar(); msgs1_msg[i] = StringVar(); msgs2_enable[i] = BooleanVar(); msgs2_addr_trig[i] = IntVar()
    msgs2_addr_data[i] = IntVar(); msgs2_msg[i] = StringVar(); msgs2_unit[i] = StringVar(); msgs2_t[i] = IntVar()

items_per_row = 3
for ii in range(12):
    Message1(page1, f"Message {ii+1}", ii // items_per_row, ii % items_per_row, msgs1_enable[ii], msgs1_addr[ii], msgs1_msg[ii])

for j in range(6):
    Message2(page2, f"Message {j+13}", j // items_per_row, j % items_per_row, msgs2_enable[j], msgs2_addr_trig[j], msgs2_addr_data[j], msgs2_msg[j], msgs2_unit[j])
    Message2_T(page2, f"Message {j+13}", (j // items_per_row) + 2, j % items_per_row, msgs2_t[j])
    Message2(page3, f"Message {j+19}", j // items_per_row, j % items_per_row, msgs2_enable[j+6], msgs2_addr_trig[j+6], msgs2_addr_data[j+6], msgs2_msg[j+6], msgs2_unit[j+6])
    Message2_T(page3, f"Message {j+19}", (j // items_per_row) + 2, j % items_per_row, msgs2_t[j+6])

root.protocol("WM_DELETE_WINDOW",  _destroy)
root.mainloop()

# app.py
# Displaying app.py.