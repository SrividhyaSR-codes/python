class FindingMousePointer:
    """Simple helper to get the current mouse pointer position."""

    def __init__(self):
        try:
            import pyautogui
            import time
        except ModuleNotFoundError as exc:
            raise ImportError("pyautogui is not installed. Install it with: pip install pyautogui") from exc
        self.pyautogui = pyautogui
        self.time = time

    def get_position(self):
        """Return the current mouse position as a tuple (x, y)."""
        return self.pyautogui.position()

    def print_position(self):
        """Print the current mouse position and return it."""
        self.time.sleep(10)  # Wait for 10 seconds before getting the position
        x, y = self.get_position()
        print(f"Mouse pointer position: ({x}, {y})")
        return x, y

if __name__ == "__main__":
    mouse = FindingMousePointer()
    mouse.print_position()
