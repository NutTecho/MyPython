from datetime import datetime, timedelta
from pprint import pprint
from time import mktime
import sys
import binance
from binance.client import Client
from tkinter import ttk
from tkinter import *


gui = Tk()
gui.geometry('500x500')
gui.title('binance trade')
myfont = "Consolas 20"
text = ""
APIKEY =  'KmmKN74wuPNFKUMN5FHLWyDOwNzW8U7Pbhl3HOVtb4t3olRV9JNA5O5aBCnvFtgh'
SECRET =  '7WTPYuPItpWIUAyghUiErXl89tkyjJrf288iwFVE27wI0BK0K2Q6Gb2qMXkgR6WP'
client =   Client(APIKEY,SECRET)

def getinfo(event=None):
    # info = client.get_symbol_info(symbol='BNBUSDT')
    # pprint(info)
    # depth = client.get_order_book(symbol='BNBUSDT',limit=20)
    # pprint(depth)
    symbol = coin.get()
    tickers = client.get_ticker(symbol = symbol)
    lastprice = float(tickers['lastPrice'])

    if lastprice > 5000:
        text = '{} : {:,.2f} ($)'.format(symbol,lastprice)
    elif lastprice > 200:
        text = '{} : {:,.3f} ($)'.format(symbol,lastprice)
    elif lastprice > 10:
        text = '{} : {:,.5f} ($)'.format(symbol,lastprice)
    else:
        text = '{} : {:,.8f} ($)'.format(symbol,lastprice)

    Lb1.delete(0,'end')
    Lb1.insert(1,text)
    pprint(tickers)
    Lb1.after(500,getinfo)
   
    

# time_res = client.get_server_time()
# dt = datetime.fromtimestamp(mktime(time.localtime(time_res['serverTime']/1000)))
# print(dt)

N1 = Label(gui,text = "Check Price",bg = "green",font = myfont)
N1.grid(row=0,column=0)

frame1 = ttk.LabelFrame(gui,text='Buy',height=20)
frame1.grid(row=1,column=0,padx=20,pady=20)

frame2 = ttk.LabelFrame(gui,text='Result',height=20)
frame2.grid(row=2,column=0,padx=20,pady=10)

coin = StringVar()
coin.set('BTCUSDT')
L1 = Label(frame1, text="select coin : ",bg = 'yellow', font = myfont,anchor = NW)
L1.grid(row=0,column=0,padx=5)

E1 = Entry(frame1,textvariable=coin,font = myfont,width=10,justify=CENTER)
E1.grid(row=0,column=1,padx=5)

B1 = Button(frame1,text="check",width = 20)
B1.bind('<Button-1>',getinfo)
B1.grid(row=1,column=0,columnspan=2,padx=10,pady=5)


Lb1 = Listbox(frame2,width = 20,font = myfont)
Lb1.grid(row=0,column=1,padx=20,pady=20)


gui.mainloop()