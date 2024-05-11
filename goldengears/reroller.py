import pyautogui
import time
import keyboard

def mvclick(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(0.05)


def start():
    
    while True:
        mvclick(952,817)
        mvclick(1556,956)
        time.sleep(0.5)
        mvclick(1753,564)
        mvclick(1684,967)
        pyautogui.click()
        for _ in range(5):
            time.sleep(3)
            pyautogui.click()
        
        for _ in range(6):
            pyautogui.click()
            time.sleep(0.5)
        time.sleep(1)
        mvclick(874,864)
        while True:
            if (keyboard.is_pressed('ctrl+c')):
                print('Continuing')
                break
            elif (keyboard.is_pressed('ctrl+q')):
                print('exiting')
                return
        mvclick(960,526)
        mvclick(1684,967)
        time.sleep(0.5)
        keyboard.press_and_release('esc')
        mvclick(1385,932)
        mvclick(1186,663)
        time.sleep(2)
        mvclick(952,817)
        

