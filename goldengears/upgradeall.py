import pyautogui
import time
import keyboard

firstcol = 168
coldiference = 215
blessingPerCol = 6
row1 = 362
row2 = 504
row3 = 800
confirmpos = (1568,989)
scrollMultiplier = 10



def scroll_page(scroll_count, direction='down'):
    scroll_count *= scrollMultiplier
    scroll_amount = 100
    if direction == 'up':
        scroll_amount *= -1

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
    try:
        while True:
            if keyboard.is_pressed('ctrl+q'):  # Check if Ctrl+Q is pressed at the start
                print("Stopping...")
                return
            
            for x in range(blessingPerCol):
                enhance()
                if keyboard.is_pressed('ctrl+q'):  # Check if Ctrl+Q is pressed between actions
                    print("Stopping...")
                    return
                next()
            setfirst()
            scroll_page(1, "up")
            setfirst()
            if (keyboard.is_pressed('ctrl+e')):
                break

        setfirst(row2)
        for x in range(blessingPerCol):
            enhance()
            next()
        setfirst(row3)
        for x in range(blessingPerCol):
            enhance()
            next()
        print("Ended the enhancements")
        return
        

    except KeyboardInterrupt:
        print("Program exited.")
