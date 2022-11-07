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


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

motor_x = Motor(Port.A)
motor_y = Motor(Port.D)

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

test()