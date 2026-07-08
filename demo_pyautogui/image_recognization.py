import os
import time
import pyautogui

pyautogui.FAILSAFE = True


def find_image_on_screen(template_path, confidence=0.8, grayscale=True):
    """Locate an image on the screen using template matching."""
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Template image not found: {template_path}")
    return pyautogui.locateOnScreen(template_path, confidence=confidence, grayscale=grayscale)


def wait_for_image(template_path, timeout=15, interval=0.5, confidence=0.8):
    """Wait until the image appears on screen or return None after timeout."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        location = find_image_on_screen(template_path, confidence=confidence)
        if location:
            return location
        time.sleep(interval)
    return None


def click_image(template_path, confidence=0.8):
    """Find the image and click the center of the matched region."""
    location = find_image_on_screen(template_path, confidence=confidence)
    if not location:
        raise FileNotFoundError(f"Image not found on screen: {template_path}")
    center = pyautogui.center(location)
    pyautogui.click(center)
    return center


def main():
    template = "button_template.png"
    print(f"Searching for {template}...")

    try:
        location = wait_for_image(template, timeout=20, confidence=0.8)
    except (FileNotFoundError, OSError) as exc:
        print(f"Image error: {exc}")
        return

    if not location:
        print("Image not found on screen.")
        return

    print(f"Found image at {location}, clicking...")
    try:
        click_image(template)
    except (FileNotFoundError, OSError) as exc:
        print(f"Image error: {exc}")
        return
    print("Click complete.")


if __name__ == "__main__":
    main()
