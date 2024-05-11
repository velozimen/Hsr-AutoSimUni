import pyautogui
import time
import keyboard

import pytesseract

from util.rerollerEnum import reroller
import config.screenshot as cnf
import util.screenshot as scrt
import cv2

from PIL import Image
import numpy as np

middlepos = (952,817)
confirmpos = (1568,989)
middleposlower = (952,827)
blessingpos = (1428,556)


def mvclick(x,y=None):
    if (y == None):
        pyautogui.moveTo(x)
        pyautogui.click()
        time.sleep(0.1)
    else:
        pyautogui.moveTo(x,y)
        pyautogui.click()
        time.sleep(0.1)


def start():
    
    while True:
        mvclick(middlepos)
        mvclick(confirmpos)
        time.sleep(0.5)
        mvclick(1753,564)
        mvclick(confirmpos)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()

        waitForText(reroller.FirstLoad)

        for _ in range(12):
            pyautogui.click()
            time.sleep(0.5)
        time.sleep(1)

        keyboard.press_and_release('ESC')
        waitForText(reroller.Blessing)
        for _ in range(3):
            if (checkIfText(reroller.Blessing)):
                pickBlessing()
            else:
                break
        
        time.sleep(1)
        keyboard.press_and_release('ESC')
        waitForText(reroller.LeaveForNow)

        mvclick(1385,932)
        mvclick(1186,663)
        waitForText(reroller.Analysis)

        mvclick(middlepos)
        time.sleep(1)
        

def waitForImage(pos : reroller):
    key,subkey = pos.value
    location = cnf.SCREENSHOT_COORDS[key][subkey]
    while True:
        tofind = scrt.takescreenshot(location)
        screenimg = Image.open(location[1])
        if (scrt.compare2(tofind,screenimg)):
            print("Matched")
            break
        time.sleep(1)

def waitForText(pos: reroller):
    key,subkey = pos.value
    location = cnf.SCREENSHOT_COORDS[key][subkey]
    while True:
        tofind = scrt.takescreenshot(location)
        txt = location[1]
        ret = pytesseract.image_to_string(tofind, lang="eng")
        if (txt in ret):
            print ("Matched")
            return ret
       
        time.sleep(1)

def checkIfText(pos: reroller):
    key,subkey = pos.value
    location = cnf.SCREENSHOT_COORDS[key][subkey]
    tofind = scrt.takescreenshot(location)
    txt = location[1]
    ret = pytesseract.image_to_string(tofind, lang="eng")
    if (txt in ret):
        return True
    return False
            
        
def pickBlessing():
        mvclick(blessingpos)
        mvclick(confirmpos)
        pyautogui.click()
        time.sleep(2)
