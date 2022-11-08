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


# Write your program here.
ev3.speaker.beep()

motor_x = Motor(Port.A)
motor_y = Motor(Port.D)
input_x = Motor(Port.B)
input_y = Motor(Port.C)

def test():
    y_angle = motor_y.angle()
    x_angle = motor_x.angle()
    motor_y.track_target(y_angle + 180)
    motor_x.track_target(x_angle + 180)
    while True:
        while motor_y.angle() != y_angle - 360:
            motor_y.track_target(y_angle - 360)
            motor_x.track_target(x_angle - 360)
        while motor_y.angle() != y_angle + 360:
            motor_y.track_target(y_angle + 360)
            motor_x.track_target(x_angle + 360) 
        
def calibrate_y():
    motor_y.reset_angle(0)
    motor_y.run_until_stalled(100, Stop.HOLD, 15)
    return motor_y.angle()

def manual_calibration():
    start_time = time.time()
    while time.time()-start_time < 4*1000:
        motor_x.track_target(input_x.angle())
        motor_y.track_target(input_y.angle())
        print(motor_x.angle(), motor_y.angle())
    motor_x.reset_angle(0)
    motor_y.reset_angle(0)
    ev3.speaker.beep()
    while time.time()-start_time < 10*1000:
        motor_x.track_target(input_x.angle())
        motor_y.track_target(input_y.angle())
        print(motor_x.angle(), motor_y.angle())

    ev3.speaker.beep()
    return [motor_x.angle(), motor_y.angle()]

def control(x_max, y_max):
    if 100 < input_x.angle() < x_max - 100 and 100 < input_y.angle() < y_max - 100:
        motor_x.track_target(input_x.angle())
        motor_y.track_target(input_y.angle())

max_values = manual_calibration()
while True:
    control(max_values[0], max_values[1])