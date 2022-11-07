import socket
import select
import sys
import time



IP_address = str("10.22.7.63")
Port = int("1024")

def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.connect((IP_address, Port))
        #server.send("ping".encode('utf-8'))
        print("connected")

        text = "Suck my nutzzz"
        for i in range(10):
            time.sleep(0.5)
            server.send(text.encode('utf-8'))

        
    except:
        print("connection failed")





connect()