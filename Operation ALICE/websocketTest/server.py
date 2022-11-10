import socket
import select
import sys
import time

import pygame, sys
from pygame.locals import *



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



#169.254.162.212
# takes the first argument from command prompt as IP address
IP_address = str("169.254.229.19")

# takes second argument from command prompt as port number
Port = int("1024")
server.bind((IP_address, Port))

server.listen(100)
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mouse_position = (0, 0)
drawing = False
screen = pygame.display.set_mode((500, 500), 0, 32)
screen.fill(WHITE)
pygame.display.set_caption("ScratchBoard")

#X = 620
#Y = 861



cordinates = ["200,200","200,400","400,400","400,200","200,200"]


conn, addr = server.accept()

while True:

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



            elif event.type == MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    pygame.draw.line(screen, BLACK, mouse_position, mouse_position, 1)
                    ms = str(mouse_position[0]) + "," + str(mouse_position[1]) + "]"

                    try:
                        conn.send(ms.encode('utf-8'))
                        print(ms)

                    
                    except:
                        print("connection failed")
                    
            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True


    pygame.display.update()
    pygame.display.flip()







conn.close()
server.close()
