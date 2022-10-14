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

motor_right = Motor(Port.A)
motor_left = Motor(Port.B)

robot = DriveBase(motor_left, motor_right, wheel_diameter=49.6, axle_track=166)
robot.settings(1000)

colorSenseR = ColorSensor(Port.S1)
colorSenseL = ColorSensor(Port.S2)

#gyro = GyroSensor(Port.S3)

ev3 = EV3Brick()
ev3.speaker.beep()

#--------------------------------------------------

maxR = 28
maxL = 35
breakToTurnValue = 50
leftLastSensed = False

highestSensL = 0

turnRate = 0
#def calibrate():
    

def current_milli_time():
    return round(time.time() * 1000)

while(True):
    senseL = colorSenseL.reflection()
    senseR = colorSenseR.reflection()
    senseSum = senseL + senseR

    if(senseL < 20):
        leftLastSensed = True
    if(senseR < 20):
        leftLastSensed = False

    if(senseSum < 80):
        turnRate = (senseL-senseR)*2
    elif(leftLastSensed):
        robot.turn(-30)
    elif(not leftLastSensed):
        robot.turn(-30)


    robot.drive(400, turnRate)

    print(senseL, senseR, leftLastSensed, senseL+senseR)


    
