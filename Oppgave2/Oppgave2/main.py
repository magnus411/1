#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



#if sensor is trykked do def()
#Utrasonis for å ungå trær 
import time
#Si exersice 2 ganger
motor_left = Motor(Port.A)
motor_right = Motor(Port.B)

robot = DriveBase(motor_left, motor_right, wheel_diameter=49.6, axle_track=105)
robot.settings(1000)
#ts = TouchSensor()

us = UltrasonicSensor(Port.S3)
ts = TouchSensor(Port.S4)

ts2 = TouchSensor(Port.S1)
ts3 = TouchSensor(Port.S2)


drive = False
done = False
ev3 = EV3Brick()
# Write your program here.
ev3.speaker.beep()


while True:
    if ts.pressed() and drive == False:
        drive = True
        ev3.speaker.say("Exersice two")


        
    while drive == True:

        

        if ts.pressed() and drive == True:
            ev3.speaker.say("Exersice Done")

            drive = False


        if us.distance() < 300:
            robot.drive(200, 0)  
            speed = us.distance()

            if us.distance() <= 100:
                robot.straight(-300)
                time.sleep(1)
                robot.turn(35)
                robot.drive(1000,0)

        else:
            robot.drive(1000, 0)

        if ts2.pressed() or ts3.pressed():
            robot.straight(-300)
            time.sleep(1)
            robot.turn(75)
            robot.drive(1000,0)


    
    robot.drive(0,0)


    


        #robot.straight()
    




    

    

    #robot.turn(90)
        


    
    #time.sleep(1)
    #ev3.speaker.say("Have a nice day")




# 
# Create your objects here.

