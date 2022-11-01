
from re import X
from turtle import right

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


motor_x = Motor(Port.A)
motor_y = Motor(Port.B)
motor_z = Motor(Port.C)

motor_x.positive_direction(right)
motor_y.positive_direction(right)

motor_x.gears([12, 36])
motor_y.gears([12, 36])

def startPoint():
    (0, 0)

def grid():
    x_min = 0
    y_min = 0
    x_max = 2000
    y_max = 2000

def control(in_x, in_y, x_max, y_max):
    motor_x.track_target(in_x * x_max)
    motor_y.track_target(in_y * y_max)

def calibrat():
    motor_x.angle(340)
    motor_y.angle(320)

