import keyboard
import os

while True:
    # press "E" to change to HUD
    keyboard.wait('e') # wait for Ctrl + F2 buttons to be pressed
    os.system("python \\Users\\yodal\\Desktop\\Projects\\Py-Glasses-HUD\\main-HUD.py") #open HUD script
    print('opening Main_HUD') #open HUD script
    os.system("taskkill /f /im python.exe") #close object detection script


#the problem is that line 9 also stops this script!?!? 

