import os
import sys
import time

# Avoid importing this script itself as the pyautogui package.
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir in sys.path:
    sys.path.remove(script_dir)

try:
    import mouse_operation
except ModuleNotFoundError as exc:
    raise SystemExit("pyautogui is not installed in the active Python environment. Install it with: pip install pyautogui") from exc

print("Starting simple mouse operations...")

# Move the mouse to a position smoothly over 1 second.
mouse_operation.moveTo(100, 100, duration=1)
time.sleep(1)

# Left click at the current mouse position.
print("Left click")
mouse_operation.click()
time.sleep(1)

# Right click at the current mouse position.
print("Right click")
mouse_operation.rightClick()
time.sleep(1)

# Double click at the current mouse position.
print("Double click")
mouse_operation.doubleClick()
time.sleep(1)

# Drag the mouse to a new position.
print("Drag to another position")
mouse_operation.dragTo(300, 300, duration=1)
time.sleep(1)

# Scroll the mouse wheel.
print("Scroll up")
mouse_operation.scroll(300)

time.sleep(1)

# Show the current mouse position.
x, y = mouse_operation.position()
print(f"Current mouse position: ({x}, {y})")
