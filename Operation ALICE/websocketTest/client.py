import socket
import select
import sys
import time


#169.254.127.126
IP_address = str("10.22.6.114")
Port = int("1024")

def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, 1024))

    while True:
        try:
            
            msg = server.recv(1024).decode('utf-8')
            print(msg)

        
        except:
            print("connection failed")





connect()