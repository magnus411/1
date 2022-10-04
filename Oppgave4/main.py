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
speedConst = 300
turnConst = 75




def Drive():
    if (colorSenseR.reflection() < colorConst):
        robot.drive(speedConst, turnConst)
    elif(colorSenseL.reflection() < colorConst):
        robot.drive(speedConst, -turnConst)
    else:
        robot.drive(speedConst, 0)



while(True):
    Drive()


    
