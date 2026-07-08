# Python RPA Overview

This repository contains Python examples for Robotic Process Automation (RPA) using desktop automation and browser automation.

## What is RPA?

Robotic Process Automation automates repetitive tasks by controlling the mouse, keyboard, and browser actions programmatically. In this repo:

- `pyautogui` is used for desktop-level automation like mouse movement, clicks, keyboard typing, and image matching.
- `Playwright` is used for modern browser automation with Chromium/Firebase/WebKit.
- `Selenium` is used for legacy browser automation with ChromeDriver.

## Repository structure

- `findingmouse_pointer.py` - captures the current mouse position after a short delay.
- `mouse_operation.py` - helper functions for mouse actions using `pyautogui`.
- `image_recognization.py` - finds and clicks screen elements by image template matching.
- `keyboard_operations.py` - simulates keyboard input, hotkeys, and special key presses.
- `demo_playwright/` - browser automation examples using Playwright.
- `demo_selenium/` - browser automation examples using Selenium.

## Requirements

Use the existing local virtual environment in `python-test`:

```powershell
cd C:\Users\Vignesh\python\python
.\python-test\Scripts\activate
```

Install the required packages if not already installed:

```powershell
python -m pip install pyautogui playwright selenium
python -m playwright install
```

> Note: if you run scripts without activating the virtual environment, use the full path to the environment Python:
>
> ```powershell
> .\python-test\Scripts\python.exe script.py
> ```

## Desktop automation scripts

### `findingmouse_pointer.py`

- Purpose: show how to read the current mouse cursor position.
- Key sections:
  - imports `pyautogui` and `time`
  - waits 10 seconds so you can move the mouse
  - prints mouse coordinates

### `mouse_operation.py`

- Purpose: wrapper functions for mouse actions.
- Key functions:
  - `moveTo(x, y, duration)` - move the cursor smoothly
  - `click()` - left click
  - `rightClick()` - right click
  - `doubleClick()` - double click
  - `dragTo(x, y, duration)` - drag mouse to new coordinates
  - `scroll(amount)` - scroll wheel
  - `position()` - get current cursor position

### `image_recognization.py`

- Purpose: find screen elements by image recognition and click them.
- Key sections:
  - `find_image_on_screen(template_path, confidence, grayscale)`
  - `wait_for_image(template_path, timeout, interval, confidence)`
  - `click_image(template_path, confidence)`
- Notes:
  - the script expects a template image like `button_template.png`
  - it uses `pyautogui.locateOnScreen` to match the image on the screen

### `keyboard_operations.py`

- Purpose: demonstrate keyboard automation.
- Key sections:
  - typing text with `pyautogui.write(...)`
  - pressing special keys like `enter`, `tab`, `backspace`, `esc`, `space`
  - using `pyautogui.hotkey(...)` for key combinations
  - demonstrating function keys and arrow keys

## Browser automation scripts

### Playwright examples (`demo_playwright/`)

The `demo_playwright` folder contains Playwright examples using both sync and async APIs.

#### `playwright_rpa.py`

- Uses `playwright.sync_api.SyncPlaywright`
- Demonstrates:
  - opening Chromium in non-headless mode
  - navigating to Google
  - taking screenshots in `playwright_output/`
  - searching Wikipedia and capturing a page title
  - filling a contact form on W3Schools

#### `playwright_key_func.py`

- Uses `playwright.async_api.AsyncPlaywright`
- Demonstrates:
  - opening Google asynchronously
  - comments describing how to capture selectors using browser developer tools

#### `playwright_selectors.py`

- Uses `playwright.sync_api.SyncPlaywright`
- Demonstrates:
  - searching Google for `Gen AI latest updates`
  - waiting for results
  - printing the first 10 search result titles

#### `playwright_selectors2.py`

- Uses `playwright.sync_api.SyncPlaywright`
- Demonstrates:
  - navigating to Google News search results for `Generative AI`
  - printing the first article titles and links

### Selenium examples (`demo_selenium/`)

The Selenium folder contains browser automation scripts for ChromeDriver.

#### `selenium_demo.py`

- Demonstrates a simple browser launch and navigation with Selenium.
- Opens `https://the-internet.herokuapp.com`.

#### `selenium_search.py`

- Demonstrates:
  - opening Google with Selenium
  - searching for `Gen AI latest updates`
  - waiting for search results to appear
  - printing the first result titles and links

## Run commands

From repository root:

```powershell
cd C:\Users\Vignesh\python\python
.\python-test\Scripts\activate
```

Then run any demo script:

```powershell
python findingmouse_pointer.py
python mouse_operation.py
python image_recognization.py
python keyboard_operations.py
```

For Playwright demos:

```powershell
cd demo_playwright
python playwright_rpa.py
python playwright_key_func.py
python playwright_selectors.py
python playwright_selectors2.py
```

For Selenium demos:

```powershell
cd demo_selenium
python selenium_demo.py
python selenium_search.py
```

If the environment is not activated:

```powershell
cd C:\Users\Vignesh\python\python\demo_selenium
..\python-test\Scripts\python.exe selenium_search.py
```

## Notes and troubleshooting

- Do not name your script `playwright.py` or `selenium.py` in the same folder as the project, because that shadows the installed package and causes import errors.
- If you get `ModuleNotFoundError` for `playwright`, verify the correct Python interpreter is active:
  - `.\python-test\Scripts\python.exe -m pip show playwright`
- For Playwright, install browser binaries with:
  - `python -m playwright install`
- For Selenium, ensure ChromeDriver is available and compatible with your Chrome browser version.
- If Google search page structure changes, update selectors in `selenium_search.py` and `playwright_selectors.py`.

## What to learn from each section

- `findingmouse_pointer.py` and `mouse_operation.py` teach desktop pointer control.
- `image_recognization.py` teaches pixel-level GUI automation using templates.
- `keyboard_operations.py` teaches typing automation and key combinations.
- `demo_playwright/` shows modern browser automation with a powerful synchronous/async API.
- `demo_selenium/` shows Selenium-based browser automation and waits for real web page content.
