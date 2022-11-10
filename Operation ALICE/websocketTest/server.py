import socket
import select
import sys




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)




# takes the first argument from command prompt as IP address
IP_address = str("169.254.127.126")

# takes second argument from command prompt as port number
Port = int("1024")
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
import time

server.listen(100)
list_of_clients = []


conn, addr = server.accept()
while True:


    

    arr=[]
    # prints the address of the user that just connected
    print (addr[0] + " connected")
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    arr.append(msg)
    if len(arr) >= 10:
        break

    # creates and individual thread for every user
    # that connects



conn.close()
server.close()
