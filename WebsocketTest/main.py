#!/usr/bin/env pybricks-micropython
#Den ordentlige koden
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time, math, random
import socket
import select
import sys
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()


motor_x = Motor(Port.A)
motor_y = Motor(Port.D)
motor_z = Motor(Port.B)

z_button = TouchSensor(Port.S1)

ev3.speaker.beep()

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
    motor_x.run_until_stalled(-500, Stop.HOLD, 17)
    motor_x.reset_angle(0)
    motor_x.run_until_stalled(500, Stop.HOLD, 17)
    
    ev3.speaker.beep()
    return motor_x.angle()

#Gets maximum motor y angle and goes to 0,0 automatically
def autoCalibrate_y():
    motor_y.run_until_stalled(-500, Stop.HOLD, 15)
    motor_y.reset_angle(0)
    motor_y.run_until_stalled(500, Stop.HOLD, 15)

    ev3.speaker.beep()
    return motor_y.angle()

def autoCalibrate_z():
    motor_z.run_until_stalled(100, Stop.HOLD, 30)
    motor_z.reset_angle(0)
    motor_z.run_until_stalled(-100, Stop.HOLD, 30)

    ev3.speaker.beep()
    return motor_z.angle()


def draw(isDraw):
    if isDraw:
        motor_z.track_target(motor_z_max_angle)
    else:
        motor_z.track_target(0)


def connection():
    motor_x_max_angle = autoCalibrate_x()
    motor_y_max_angle = autoCalibrate_y()
    print(motor_x_max_angle)
    print(motor_y_max_angle)
    #Center x and y
    motor_x.run_target(300, motor_x_max_angle/2, Stop.HOLD, True)
    motor_y.run_target(300, motor_y_max_angle/2, Stop.HOLD, True)

    #Calibrate z and send z to startpos
    motor_z_max_angle = autoCalibrate_z()
    motor_z.run_target(100, 0, Stop.HOLD, True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("169.254.127.159", 1024))

    while True:
        try:
            print("Static test")
            msg = (server.recv(1024).decode('utf-8'))

            motor_z.track_target(motor_z_max_angle)
            
            decode = msg.split(",")
            backsplit = decode[1].split("]")
            print(backsplit)
            print(decode)
            if motor_x_max_angle > int(decode[0]) > 0:
                motor_x.track_target(int())
                
            if motor_y_max_angle > int(backsplit[0]) > 0:
                motor_y.track_target(int(backsplit[0]))

            

        
        except:
            motor_z.track_target(0)
            print("connection failed")



connection()
#Calibrate x and y 


#Port = int("1024")




    

        

def run():



    mouse_max_value_x = 2000 #size of mouse input window x axis
    mouse_max_value_y = 2000 #size of mouse input window y axis

    mouse_input_value_x = input()
    mouse_input_value_y = input()

    mouse_input_value_x = mouse_input_value_x / mouse_max_value_x * motor_x_max_angle
    mouse_input_value_y = mouse_input_value_y / mouse_max_value_y * motor_y_max_angle

    motor_x.track_target(mouse_input_value_x)
    motor_y.track_target(mouse_input_value_y)

def draw(isDraw):
    if isDraw:
        motor_z.track_target(motor_z_max_angle)
    else:
        motor_z.track_target(0)


    



