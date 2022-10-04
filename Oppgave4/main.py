#!/usr/bin/env pybricks-micropython
#^^^ MÅ VÆRE MED SOM FØRSTE LINJE^^^
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random


import time

motor_left = Motor(Port.A)
motor_right = Motor(Port.B)

robot = DriveBase(motor_left, motor_right, wheel_diameter=49.6, axle_track=125)
robot.settings(1000)

colorSenseR = ColorSensor(Port.S1)
colorSenseL = ColorSensor(Port.S2)

ev3 = EV3Brick()
ev3.speaker.beep()

colorConst = 30
speedConst = 2
turnConst = 10

#Sens max100 min 6
#Sens max89  min 6

#Diff sens1 - sens2 = 90
#diff sens1 - sens2 = -79
#diff sens1 - sens2 = 10


def Drive():
    turnRate =  (colorSenseL.reflection() - colorSenseR.reflection() + 12)
    driveRate = (colorSenseL.reflection() + colorSenseR.reflection() - 90) * speedConst

    #print(turnRate)
    robot.drive(driveRate, turnRate)


#
 #   if (colorSenseR.reflection() < colorConst):
  #      robot.drive(speedConst, turnConst)
#    elif(colorSenseL.reflection() < colorConst):
#        robot.drive(speedConst, -turnConst)
#    else:
#       robot.drive(speedConst, 0)



while(True):
    
    Drive()


    
