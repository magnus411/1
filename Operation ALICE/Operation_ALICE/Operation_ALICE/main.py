#!/usr/bin/env pybricks-micropython
#Den ordentlige koden
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

ev3 = EV3Brick()

motor_x = Motor(Port.A)
motor_y = Motor(Port.D)

#Gets maximum motor x angle
def calibrate_x():
    motor_x.reset_angle(0)
    motor_x.run_until_stalled(100, Stop.HOLD, 10)
    return motor_x.angle()

#Gets maximum motor y angle
def calibrate_y():
    motor_y.reset_angle(0)
    motor_y.run_until_stalled(100, Stop.HOLD, 10)
    return motor_y.angle()

#Gets maximum motor x angle and goes to 0,0 automatically
def autoCalibrate_x():
    motor_x.run_until_stalled(-200, Stop.HOLD, 15)
    motor_x.reset_angle(0)
    motor_x.run_until_stalled(200, Stop.HOLD, 15)
    return motor_x.angle()

#Gets maximum motor y angle and goes to 0,0 automatically
def autoCalibrate_y():
    motor_y.run_until_stalled(-200, Stop.HOLD, 15)
    motor_y.reset_angle(0)
    motor_y.run_until_stalled(200, Stop.HOLD, 15)
    return motor_y.angle()

#motor_x_max_angle = calibrate_x()
#motor_y_max_angle = calibrate_y()

def run():
    mouse_max_value_x = 2000 #size of mouse input window x axis
    mouse_max_value_y = 2000 #size of mouse input window y axis

    mouse_input_value_x = input()
    mouse_input_value_y = input()

    mouse_input_value_x = mouse_input_value_x / mouse_max_value_x * motor_x_max_angle
    mouse_input_value_y = mouse_input_value_y / mouse_max_value_y * motor_y_max_angle

    motor_x.track_target(mouse_input_value_x)
    motor_y.track_target(mouse_input_value_y)

#while True:
#    run()

print(autoCalibrate_x())
print(autoCalibrate_y())