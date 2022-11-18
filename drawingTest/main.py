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
    motor_x.run_until_stalled(-500, Stop.HOLD, 20)
    motor_x.reset_angle(0)
    motor_x.run_until_stalled(500, Stop.HOLD, 20)
    
    ev3.speaker.beep()
    return motor_x.angle()

#Gets maximum motor y angle and goes to 0,0 automatically
def autoCalibrate_y():
    motor_y.run_until_stalled(-500, Stop.HOLD, 16)
    motor_y.reset_angle(0)
    motor_y.run_until_stalled(500, Stop.HOLD, 16)

    ev3.speaker.beep()
    return motor_y.angle()

def autoCalibrate_z():
    motor_z.run_until_stalled(100, Stop.HOLD, 30)
    motor_z.reset_angle(0)
    motor_z.run_until_stalled(-100, Stop.HOLD, 30)

    ev3.speaker.beep()
    return motor_z.angle()

def turboCalibrate_xy():
    motor_x.run_until_stalled(-500, Stop.HOLD, 17)
    motor_x.reset_angle(0)

    motor_x.run_target(300, 50, Stop.HOLD, True)

    motor_y.run_until_stalled(-500, Stop.HOLD, 13)
    motor_y.reset_angle(0)

    ev3.speaker.beep()
    return [700,700]

#Calibrate x and y 
motor_y_max_angle = autoCalibrate_y()
motor_y.run_target(300, 0, Stop.HOLD, True)
motor_x_max_angle = autoCalibrate_x()

print(motor_x_max_angle, motor_y_max_angle)

#Center x and y
motor_x.run_target(300, motor_x_max_angle/2, Stop.HOLD, True)
motor_y.run_target(300, motor_y_max_angle/2, Stop.HOLD, True)

#Calibrate z and send z to startpos
motor_z_max_angle = autoCalibrate_z()
print(motor_z_max_angle)

def draw(isDraw):
    if isDraw:
        motor_z.track_target(motor_z_max_angle*0.85)
    else:
        motor_z.track_target(0)

draw(False)

def run():
    mouse_max_value_x = 2000 #size of mouse input window x axis
    mouse_max_value_y = 2000 #size of mouse input window y axis

    mouse_input_value_x = input()
    mouse_input_value_y = input()

    mouse_input_value_x = mouse_input_value_x / mouse_max_value_x * motor_x_max_angle
    mouse_input_value_y = mouse_input_value_y / mouse_max_value_y * motor_y_max_angle

    motor_x.track_target(mouse_input_value_x)
    motor_y.track_target(mouse_input_value_y)

def go2x(val):
    if 0 <= val < motor_x_max_angle:
        motor_x.run_target(300, val, Stop.HOLD, True)

def go2y(val):
    if 0 <= val < motor_y_max_angle:
        motor_y.run_target(300, val, Stop.HOLD, True)

def go2xy(x, y):
    x, y = int(x), int(y)
    if 0 < x < motor_x_max_angle and 0 < y < motor_y_max_angle:
        while motor_x.angle() != x or motor_y.angle() != y:
            motor_x.track_target(x)
            motor_y.track_target(y)

def drawPixelSquare(x, y, pixelValue, maxSize):
    change = maxSize*pixelValue/2
    go2x(x-change)
    go2y(y-change)
    draw(True)
    go2x(x+change)
    go2y(y+change)
    go2x(x-change)
    go2y(y-change)
    draw(False)

def drawPixelCross(x, y, pixelValue, maxSize):
    change = maxSize*pixelValue/2
    if 0.4 < pixelValue < 0.7:
        go2xy(x-change, y-change)
        draw(True)
        go2xy(x+change, y+change)
        draw(False)
        go2xy(x-change, y+change)
        draw(True)
        go2xy(x+change, y-change)
        draw(False)


def drawGrid(xPixels, yPixels):
    xCanvas = [0+50, motor_x_max_angle-50]
    yCanvas = [0+50, motor_y_max_angle-50]
    center = [xCanvas[0]+(xCanvas[1]-xCanvas[0])/2, yCanvas[0]+(yCanvas[1]-yCanvas[0])/2]
    for i in range(yCanvas[0], yCanvas[1], int(motor_y_max_angle/yPixels)):
        for j in range(xCanvas[0], xCanvas[1], int(motor_x_max_angle/xPixels)):
            drawPixelCross(j, i, ((1-abs(center[0]-j)/center[0])*(1-abs(center[1]-i)/center[1])), 50)

def drawSine(levels):
    xCanvas = [0+50, motor_x_max_angle-50]
    yCanvas = [0+50, motor_y_max_angle-50]
    center = [xCanvas[0]+(xCanvas[1]-xCanvas[0])/2, yCanvas[0]+(yCanvas[1]-yCanvas[0])/2]
    for i in range(yCanvas[0], yCanvas[1], int(motor_y_max_angle/levels)):
        draw(False)
        go2xy(xCanvas[0], i)
        draw(True)
        for j in range(xCanvas[0], xCanvas[1]):
            #change = ((1-abs(center[0]-j)/center[0])*(1-abs(center[1]-i)/center[1]))
            change = 1-math.sqrt((center[0]-j)**2/center[0]**2 + (center[1]-i)**2/center[1]**2)
            newy = int(i + math.sin(j*50)*change*50)
            motor_x.track_target(j)
            while motor_y.angle() != newy:
                motor_y.track_target(newy)


