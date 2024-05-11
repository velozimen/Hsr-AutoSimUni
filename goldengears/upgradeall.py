import pyautogui
import time
import keyboard

def scroll_page(scroll_count, direction='down'):
    scroll_count *= 10
    scroll_amount = 1000  # Positive for scrolling down, negative for scrolling up
    if direction == 'up':
        scroll_amount *= -1

    for _ in range(scroll_count):
        pyautogui.scroll(scroll_amount)
        time.sleep(0.001)  # Add a slight delay between scrolls for smoother execution

def enhance():
    initial = pyautogui.position()
    pyautogui.moveTo(1568,989)
    for _ in range(10):
        pyautogui.click()
        time.sleep(0.001)
    pyautogui.moveTo(initial)

def next():
    pyautogui.drag(215)

def setfirst(row=1):
    if (row == 1):
        pyautogui.moveTo(168,362)
    elif (row == 2):
        pyautogui.moveTo(168,504)
    else:
        pyautogui.moveTo(168,800)
    pyautogui.click()

# Example usage
def start():
    setfirst()
    try:
        while True:
            if keyboard.is_pressed('ctrl+q'):  # Check if Ctrl+Q is pressed at the start
                print("Stopping...")
                return
            
            for x in range(6):
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

        setfirst(2)
        for x in range(6):
            enhance()
            next()
        setfirst(3)
        for x in range(6):
            enhance()
            next()
        print("Ended the enhancements")
        return
        

    except KeyboardInterrupt:
        print("Program exited.")
