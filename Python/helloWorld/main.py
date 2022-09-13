#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()




def run():
    ev3.screen.print("Hello World!")
    

    motor_left = Motor(Port.A)
    motor_right = Motor(Port.B)

    robot = DriveBase(motor_left, motor_right, wheel_diameter=49.6, axle_track=105)
    robot.settings(1000)

    for i in range(3):
        robot.straight(100)
        robot.turn(90)
        


    
    time.sleep(1)
    ev3.speaker.say("Have a nice day")





# Write your program here.



run()    
