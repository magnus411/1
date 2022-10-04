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

ultraSense = UltrasonicSensor(Port.S3)

colorSenseR = ColorSensor(Port.S1)
colorSenseL = ColorSensor(Port.S2)

ev3 = EV3Brick()
ev3.speaker.beep()

colorConst = 20
speedConst = 150
turnConst = 100

last_time = time.time()


def Drive():
    if (colorSenseR.reflection() < colorConst):
        robot.drive(speedConst, turnConst)
    elif(colorSenseL.reflection() < colorConst):
        robot.drive(speedConst, -turnConst)
    else:
        robot.drive(speedConst, 0)

def SensObject():
    if(ultraSense.distance() < 200):
        ev3.speaker.beep(300, 1000)
        return False
    else:
        return True

def Dance1():
    time.sleep(0.5)
    robot.turn(360)
    time.sleep(0.5)
    

def Dance2():
    robot.straight(100)
    time.sleep(0.5)
    robot.straight(-200)
    time.sleep(0.5)
    robot.straight(200)
    time.sleep(0.5)
    robot.straight(-100)
    time.sleep(0.5)


def Dance3():
    robot.turn(10)
    robot.turn(-10)
    robot.turn(10)
    robot.turn(-10)
    robot.turn(10)
    robot.turn(-10)

def Dance4():
    robot.turn(90)
    robot.straight(-200)
    robot.turn(180)
    robot.straight(-200)
    robot.turn(90)
    
def ChooseDance(number):
    if number == 1:
        Dance1()
    elif number == 2:
        Dance2()
    elif number == 3:
        Dance3()
    elif number == 4:
        Dance4()



while(SensObject()):
    Drive()

    current_time = time.time()

    if current_time - last_time >= 10:
        ChooseDance(random.randint(1,4))
        last_time = current_time



def Drive():
    if (colorSenseR.reflection() < colorConst):
        robot.drive(speedConst, turnConst)
    elif(colorSenseL.reflection() < colorConst):
        robot.drive(speedConst, -turnConst)
    else:
        robot.drive(speedConst, 0)

