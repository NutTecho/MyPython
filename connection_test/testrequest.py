import requests
import socket
import sys
from pprint import pprint

print("hello")
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket success")
except socket.error as err:
    print("socket error")

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit() 

port = 80
s.connect((host_ip,port))
# session = requests.Session()
# response = session.get('http://localhost:3000/showchart' )

# x = requests.get()

# pprint(response.json())

def mainrun():
    host = "127.0.0.1"
    port = 5000
    server = socket.socket()
    server.bind((host,port))
    server.listen(1)
    print("waiting client....")
    client,addr = server.accept()
    print("connect from " +str(addr))
    while True:
        data = client.recv(1024).decode('utf-8')
