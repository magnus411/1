import pyautogui
import time
from pynput import*

def get_coords (x, y):
    print ("now at: {}" .format((x, y)))

with mouse.Listener(on_move = get_coords) as listen:
    listen.join()

'''time.sleep(3)
distance = 300
while distance > 0:
    pyautogui.dragRel (distance, 0, 1, button = "left")
    distance = distance - 20
    pyautogui.dragRel (0, distance, 1, button = "left")
    pyautogui.dragRel (-distance, 0, 1, button = "left")
    distance = distance -20
    pyautogui.dragRel (0, -distance, 1, button = "left")
    time.sleep(2)'''
    
def mindstormDrawing():
    distance = 300
    while distance > 0:
        motor_x.run_target(200, distance, Stop.HOLD, True)
        distance = distance -20
        motor_y.run_target(200, -distance, Stop.HOLD, True)
        motor_x.run_target(200, -distance, Stop.HOLD, True)
        distance = distance -20
        motor_y.run_target(200, distance, Stop.HOLD, True)
