import threading
import time
from pynput import keyboard
from pynput.keyboard import Controller, Key

keyboard_controller = Controller()
spamming = False
toggle_key = Key.f8  # Change this to your preferred toggle key

def spam_e():
    while True:
        if spamming:
            keyboard_controller.press('e')
            keyboard_controller.release('e')
            time.sleep(0.05)  # Adjust the delay between key presses
        else:
            time.sleep(0.1)

def on_press(key):
    global spamming
    if key == toggle_key:
        spamming = not spamming
        print(f"Spamming {'enabled' if spamming else 'disabled'}.")

# Start the spamming thread
threading.Thread(target=spam_e, daemon=True).start()

# Start the key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
