import socket
import select
import sys
import time



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



#169.254.162.212
# takes the first argument from command prompt as IP address
IP_address = str("10.22.6.114")

# takes second argument from command prompt as port number
Port = int("1024")
server.bind((IP_address, Port))

server.listen(100)



#X = 620
#Y = 861



cordinates = ["200,200","200,400","400,400","400,200","200,200"]


conn, addr = server.accept()

while True:



        try:
            text="asdasd"
            conn.send(text.encode('utf-8'))

        
        except:
            print("connection failed")
        








conn.close()
server.close()
