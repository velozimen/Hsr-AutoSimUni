import pyautogui
import time
import keyboard
import findBlessingPage as fbp

firstcol = 168
coldiference = 215
blessingPerCol = 6
row1 = 362
row2 = 504
row3 = 800
confirmpos = (1568,989)
scrollMultiplier = 10
number = fbp.start()
print(number)


def scroll_page(scroll_count, direction='down'):
    scroll_count *= scrollMultiplier
    scroll_amount = -95

    for _ in range(scroll_count):
        pyautogui.scroll(scroll_amount)
        time.sleep(0.001)  
        
def enhance():
    initial = pyautogui.position()
    pyautogui.moveTo(confirmpos)
    for _ in range(10):
        pyautogui.click()
        time.sleep(0.001)
    pyautogui.moveTo(initial)

def next():
    pyautogui.drag(coldiference)

def setfirst(row=row1):
    pyautogui.moveTo(firstcol,row)
    pyautogui.click()

# Example usage
def start():
    setfirst()
    current = 1
    numOfRows = (number // blessingPerCol) +1
    for _ in range(numOfRows -2):
        for _ in range(blessingPerCol):
            enhance()
            next()

        setfirst()
        scroll_page(1, "up")
        setfirst()

    setfirst(row2)
    for _ in range(blessingPerCol):
        enhance()
        next()
    setfirst(row3)
    for _ in range(blessingPerCol *numOfRows - number):
        enhance()
        next()
    print("Ended the enhancements")
    return
time.sleep(2)
start()