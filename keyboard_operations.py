import time

try:
    import pyautogui
except ModuleNotFoundError as exc:
    raise SystemExit("pyautogui is not installed. Install it with: pip install pyautogui") from exc

print("Keyboard operations demo started...")
print("Place your cursor in a text field, then wait a moment...")
time.sleep(2)

try:
    # Type harmless text into whatever window is active.
    pyautogui.write("Demo text for keyboard automation", interval=0.1)
    pyautogui.press("enter")
    time.sleep(1)

    # Single key press
    pyautogui.press("tab")
    time.sleep(1)
        

    # Press multiple keys together
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)

    # Ctrl+C can interrupt the terminal, so this example uses a safe shortcut.
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Special keys examples
    pyautogui.press("backspace")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(1)

    # Function keys
    for key in ["f1", "f2", "f3"]:
        pyautogui.press(key)
        time.sleep(0.3)

    # Arrow keys
    for key in ["up", "down", "left", "right"]:
        pyautogui.press(key)
        time.sleep(0.3)

    # Hold a key down and release it
    pyautogui.keyDown("shift")
    pyautogui.press("left")
    pyautogui.keyUp("shift")

    time.sleep(1)
    print("Keyboard operations demo completed.")
except KeyboardInterrupt:
    print("\nKeyboard demo interrupted by user.")
