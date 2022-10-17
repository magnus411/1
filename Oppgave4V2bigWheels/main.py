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

robot = DriveBase(motor_left, motor_right, wheel_diameter=81.6, axle_track=160)
robot.settings(1000, 100, 100)

colorSenseR = ColorSensor(Port.S1)
colorSenseL = ColorSensor(Port.S2)
pushButton = TouchSensor(Port.S3)
gyro = GyroSensor(Port.S4)

#gyro = GyroSensor(Port.S3)

ev3 = EV3Brick()
ev3.speaker.beep()

#--------------------------------------------------

maxR = 28
maxL = 35
breakToTurnValue = 50
leftLastSensed = False
drive = False

highestSensL = 0

turnRate = 0
driveRate = 300
#def calibrate():
    

def current_milli_time():
    return round(time.time() * 1000)


while True:
    senseL = colorSenseL.reflection()
    senseR = colorSenseR.reflection()
    senseSum = senseL + senseR

    if pushButton.pressed():
        if drive:
            drive = False
        else:
            drive = True

    if drive:

        if senseL < 20:
            leftLastSensed = True
        if senseR < 20:
            leftLastSensed = False
            
        if senseSum > 80:
            onLine = False
        else:
            onLine = True

        #Kode for når roboten er på lija
        if onLine:
            turnRate = (senseL-senseR)* 3.3 * (1.3-(driveRate/500))

            #Roboten kjører nær maksfart når den har vært på linja i under 750mm
            if robot.distance() < 550:
                if driveRate < 400:
                    driveRate += 2
            else:
                if driveRate > 200:
                    driveRate -= 5


        elif leftLastSensed:
            if driveRate > 100:
                driveRate -= 20
            if turnRate > -100:
                turnRate -= 6

            robot.reset()
            #turnRate -= 1 
            #driveRate = 0
            #robot.turn(-10)
            pass
        elif not leftLastSensed:
            if driveRate > 100:
                driveRate -= 20
            if turnRate < 100:
                turnRate += 6

            robot.reset()
            #turnRate += 1 
            #driveRate = 0
            #robot.turn(10)
            pass

        if gyro.angle() > 80 or gyro.angle() < -80:
            robot.reset()
            gyro.reset_angle(0)


        robot.drive(driveRate, turnRate)

        print(senseL, senseR, gyro.angle(), senseL+senseR)

    else:
        robot.drive(0, 0)

"""
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
        driveRate = 300
    elif(leftLastSensed):
        turnRate -= 1 
        driveRate = 50
    elif(not leftLastSensed):
        turnRate += 1 
        turnRate = 50


    robot.drive(driveRate, turnRate)

    print(senseL, senseR, leftLastSensed, senseL+senseR)
"""