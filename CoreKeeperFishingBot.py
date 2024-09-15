from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
#Libs

#By @LePoulet12 :)
print("Simple Auto-Fishing for CoreKeeper by @LePoulet12")

#Click
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(1.0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

#Variables
forcedClick = 0
numberOfReels = 0

#Scalling important variables
screen_width, screen_height = pyautogui.size()
reference_width = 1920
reference_height = 1080
fish_x = int(968 * screen_width / reference_width)
fish_y = int(370 * screen_height / reference_height)
click_x = int(947 * screen_width / reference_width)
click_y = int(435 * screen_height / reference_height)

while not keyboard.is_pressed('z'):
    if forcedClick >= 24:
        #force click if no fish or bugged
        print("Forced Click")
        click(click_x, click_y)
        numberOfReels += 1
        print("Reel #"+str(numberOfReels))
        forcedClick = 0

    if pyautogui.pixel(fish_x,fish_y)[0] == 224 and pyautogui.pixel(fish_x,fish_y)[1] == 224 and pyautogui.pixel(fish_x,fish_y)[2] == 234:
        #catching a fish
        print("found fish")
        click(click_x, click_y)
        numberOfReels += 1
        print("Reel #"+str(numberOfReels))
        forcedClick = 0
    else:
        #No fish
        forcedClick += 1
        time.sleep(0.30)

  
