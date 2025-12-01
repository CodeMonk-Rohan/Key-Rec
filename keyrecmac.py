import os
from datetime import datetime
from pynput import keyboard  # pip install pynput

# === HOTKEYS DICTIONARY (MAPPING) ===
# Adapted for pynput (Mac friendly)
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
    "caps_lock": " [CAPSLOCK] ",
    "esc": " [ESC] ",
    "delete": " [DEL] ",
    "home": " [HOME] ",
    "end": " [END] ",
    "page_up": " [PGUP] ",
    "page_down": " [PGDN] ",
    
    # --- Mac Specific Modifiers ---
    "cmd": " [CMD] ",       # Command (Left)
    "cmd_r": " [CMD] ",     # Command (Right)
    "shift": " [SHIFT] ",
    "shift_r": " [SHIFT] ",
    "ctrl": " [CTRL] ",
    "ctrl_r": " [CTRL] ",
    "alt": " [OPT] ",       # Option/Alt
    "alt_r": " [OPT] ",

    # --- Arrows ---
    "up": " [UP] ", "down": " [DOWN] ", "left": " [LEFT] ", "right": " [RIGHT] "
}

# === SETUP LOG FILE ===
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file_path = os.path.join(desktop_path, "mac_shortcut_log.txt")

def on_press(key):
    """
    This function runs every time a key is pressed.
    """
    try:
        # Try to get the actual character (handles a vs A automatically on Mac)
        # pynput returns 'A' if shift is held, and 'a' if not.
        key_name = key.char
        label = key_name  # Default to just logging the character
    except AttributeError:
        # It's a special key (like Key.space, Key.cmd, etc.)
        # We strip the 'Key.' prefix to get the name (e.g., "space")
        key_name = str(key).replace("Key.", "")
        
        # Check mapping
        if key_name in KEY_MAPPING:
            label = KEY_MAPPING[key_name]
        else:
            label = f" [{key_name.upper()}] "

    # Create timestamped entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Only log if it's a valid character or a known special key
    if key_name:
        entry = f"{timestamp} | Key: {key_name} | Mapped: {label}\n"
        
        try:
            with open(log_file_path, "a", encoding="utf-8") as f:
                f.write(entry)
            print(entry, end="")
        except Exception as e:
            print(f"Error: {e}")

def main():
    print(f"--- Mac KeyRec Started ---")
    print(f"Logging to: {log_file_path}")
    print("Press CTRL+C to stop.")
    print("NOTE: Ensure your Terminal has 'Input Monitoring' permissions in System Settings.")

    # Start the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()