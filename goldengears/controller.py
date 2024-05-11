import upgradeall as upg
import reroller as reroll
import keyboard
import time

def start_upgrade():
    print("Upgrade starting...")
    upg.start()

def start_reroll():
    print("Reroll starting...")
    reroll.start()

def exit_script():
    print("Exiting...")
    return "Exit"

def listen_for_hotkeys():
    keyboard.add_hotkey('ctrl+w', start_upgrade) # ctrl + e last rows, ctrl + q to stop
    keyboard.add_hotkey('ctrl+r', start_reroll)

listen_for_hotkeys()
def start():
    while True:
        if (keyboard.is_pressed('ctrl+x')):
            print('Stopped')
            return
        time.sleep(0.2)
        

start()

