import upgradeall as upg
import reroller as reroll
import keyboard

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
    keyboard.add_hotkey('ctrl+r', start_reroll) # ctrl + c continue loop, ctrl + q to stop

listen_for_hotkeys()
def start():
    while True:
        if (keyboard.is_pressed('ctrl+x')):
            print('Stopped')
            return

start()

