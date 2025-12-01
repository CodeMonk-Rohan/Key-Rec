import os
from datetime import datetime
import keyboard  # pip install keyboard

# === HOTKEYS DICTIONARY (MAPPING) ===
# This maps the raw key name (from the library) to your desired log format.
KEY_MAPPING = {
    # --- Numbers ---
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", 
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",

    # --- Punctuation ---
    "`": "`", "-": "-", "=": "=", "[": "[", "]": "]", "\\": "\\",
    ";": ";", "'": "'", ",": ",", ".": ".", "/": "/", 
    
    # --- Special Keys ---
    "space": " [SPACE] ",
    "enter": " [ENTER]\n",
    "backspace": " [BACKSPACE] ",
    "tab": " [TAB] ",
    "caps lock": " [CAPSLOCK] ",
    "esc": " [ESC] ",
    "delete": " [DEL] ",
    "insert": " [INS] ",
    "home": " [HOME] ",
    "end": " [END] ",
    "page up": " [PGUP] ",
    "page down": " [PGDN] ",
    "print screen": " [PRINTSCR] ",
    
    # --- Modifier Keys ---
    "shift": " [SHIFT] ",
    "ctrl": " [CTRL] ",
    "alt": " [ALT] ",
    "right shift": " [SHIFT] ",
    "right ctrl": " [CTRL] ",
    "right alt": " [ALT] ",
    "left windows": " [WIN] ",
    "right windows": " [WIN] ",

    # --- Arrows ---
    "up": " [UP] ", "down": " [DOWN] ", "left": " [LEFT] ", "right": " [RIGHT] "
}

# === SETUP LOG FILE ===
# Saves directly to your desktop for easy finding
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file_path = os.path.join(desktop_path, "shortcut_log.txt")

def log_event(event):
    """
    This function runs every time a key is pressed.
    """
    key_name = event.name.lower()
    
    # 1. Check if the key is in our mapping dictionary (Special keys, numbers, etc.)
    if key_name in KEY_MAPPING:
        label = KEY_MAPPING[key_name]
    
    # 2. Check if it is a simple letter (a-z)
    # We handle this dynamically to support both 'b' and 'B' based on Shift
    elif len(key_name) == 1 and key_name.isalpha():
        if keyboard.is_pressed('shift'):
            label = key_name.upper()  # Shift is held -> Uppercase
        else:
            label = key_name.lower()  # Shift not held -> Lowercase

    # 3. Fallback for any keys we missed
    else:
        label = f" [{key_name.upper()}] "

    # Create the timestamped entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} | Key: {key_name} | Mapped: {label}\n"

    # Write to file
    try:
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(entry)
        print(entry, end="")  # Also print to terminal so you know it works
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    print(f"--- KeyRec Started ---")
    print(f"Logging to: {log_file_path}")
    print("Press CTRL+C to stop.")

    # 'on_press' is efficient: it installs one global hook for everything
    keyboard.on_press(log_event)

    # Keep the script running
    keyboard.wait()

if __name__ == "__main__":
    main()