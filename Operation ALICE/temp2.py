
from re import X
from turtle import right
import pyautogui

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()


motor_x = Motor(Port.A)
motor_y = Motor(Port.B)
motor_z = Motor(Port.C)

motor_x.positive_direction(right)
motor_y.positive_direction(right)

motor_x.gears([12, 36])
motor_y.gears([12, 36])

def calibration():
    time.sleep(2)
    motor_x.reset_angle(0)
    motor_y.reset_angle(0)
    ev3.speaker.beep()
    time.sleep(2)
    ev3.speaker.beep()
    return [motor_x.angle(), motor_y.angle()]



def startPoint():
    (0, 0)

maxX = 100
maxY = 100
distance =50

def control(in_x, in_y, x_local_max, y_local_max):
    motor_x.track_target(in_x * x_local_max)
    motor_y.track_target(in_y * y_local_max)

max_pos = calibration()

control(distance, 0, maxX, maxY)
control(0, distance, maxX, maxY)
distance = -20
control(distance, 0, maxX, maxY)
control(0, distance, maxX, maxY)