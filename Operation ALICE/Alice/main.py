#!/usr/bin/env pybricks-micropython
#Den ordentlige koden
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

import pygame, sys
from pygame.locals import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mouse_position = (0, 0)
drawing = False
screen = pygame.display.set_mode((500, 500), 0, 32)
screen.fill(WHITE)
pygame.display.set_caption("ScratchBoard")



def run():
    ev3.screen.print("Hello World!")
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        mouse_position = pygame.mouse.get_pos()
        print(mouse_position)
            

        pygame.display.update()
        pygame.display.flip()


    motor_x = Motor(Port.A)
    #motor_y = Motor(Port.B)

    motor_x.run_target(100, 720, Stop.HOLD, False)
    #motor_y.run_target(100, 360, Stop.HOLD, False)

    time.sleep(1)
    ev3.speaker.say("Have a nice day")

run()