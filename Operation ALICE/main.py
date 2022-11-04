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

def test():
    motor_x = Motor(Port.A)
    motor_y = Motor(Port.D)

    motor_x.track_target(300)
    motor_y.track_target(300)

def run():
    motor_x = Motor(Port.A)
    motor_y = Motor(Port.D)

    

    motor_x.run_target(100, 720, Stop.HOLD, False)
    motor_y.run_target(100, 360, Stop.HOLD, False)

test()