# src/utils/clipboard.py

import time
import threading
import pyperclip


def copy_to_clipboard(text: str, timeout: int = 10):
    """
    Copies text to the clipboard, then clears after timeout seconds.
    """
    pyperclip.copy(text)
    print(f"Password copied to clipboard for {timeout} seconds.")

    def clear():
        time.sleep(timeout)
        pyperclip.copy("")
        print("Clipboard cleared.")

    threading.Thread(target=clear, daemon=True).start()
