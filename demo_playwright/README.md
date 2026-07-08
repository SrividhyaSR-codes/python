# demo_playwright

This folder contains a small Playwright automation demo for Python.

## Overview

- `playwright_rpa.py` - A synchronous Playwright script that demonstrates basic browser automation: visiting pages, taking screenshots, filling a form, and capturing text.
- `playwright_key_func.py` - An asynchronous Playwright example that opens Google and includes notes on using selectors.
- `playwright_selectors.py` - A synchronous demo that searches Google for "Gen AI latest updates" and prints the first result titles.
- `playwright_selectors2.py` - A synchronous demo that navigates to Google News search results for "Generative AI" and prints the first article titles and links.

## What is Playwright?

Playwright is a browser automation library from Microsoft that lets you script web browsers for testing, scraping, RPA, and automation. It supports Chromium, Firefox, and WebKit, and offers both synchronous and asynchronous Python APIs.

## Key Playwright functions and concepts

- `playwright.chromium.launch(...)` / `playwright.firefox.launch(...)` / `playwright.webkit.launch(...)` - start a browser instance.
- `browser.new_context(...)` - create an isolated browser context with independent cookies/storage.
- `context.new_page()` - open a new tab/page in that context.
- `page.goto(url)` - navigate to a URL.
- `page.fill(selector, text)` - enter text into an input field.
- `page.click(selector)` - click an element on the page.
- `page.locator(selector)` - create a locator to query and interact with elements safely.
- `page.wait_for_selector(selector)` - wait until an element appears in the DOM.
- `page.wait_for_load_state(state)` - wait for the page load state, such as `networkidle`.
- `page.screenshot(path=...)` - take a screenshot of the page.
- `page.keyboard.press(key)` - send keyboard input to the page.
- `browser.close()` - shut down the browser.

## Requirements

- Python 3.11+ (or the version in the existing `python-test` virtual environment)
- Playwright installed in the environment
- Browser binaries installed via Playwright if not already present

## Recommended setup

Use the existing virtual environment in the repository:

```powershell
cd C:\Users\Vignesh\python\python
.\python-test\Scripts\activate
python -m pip install playwright
python -m playwright install
```

If you prefer not to activate the venv, run directly using its Python executable:

```powershell
cd C:\Users\Vignesh\python\python
.\python-test\Scripts\python.exe -m pip install playwright
.\python-test\Scripts\python.exe -m playwright install
```

## Run a demo script

From the `demo_playwright` folder:

```powershell
cd C:\Users\Vignesh\python\python\demo_playwright
.\..\python-test\Scripts\python.exe .\playwright_rpa.py
```

Or after activating the virtual environment:

```powershell
cd C:\Users\Vignesh\python\python\demo_playwright
python .\playwright_rpa.py
```

## Script descriptions

### `playwright_rpa.py`
- Uses `playwright.sync_api`
- Opens Chromium in non-headless mode
- Visits `https://www.google.com`
- Navigates to `https://www.wikipedia.org/` and performs a search
- Visits a W3Schools contact form and fills it out
- Saves screenshot files under `playwright_output/`

### `playwright_key_func.py`
- Uses `playwright.async_api`
- Opens Google in Chromium
- Includes comments about inspecting page selectors with developer tools
- Demonstrates how to run an async Playwright script with `asyncio`

### `playwright_selectors.py`
- Uses `playwright.sync_api`
- Opens Google and searches for `Gen AI latest updates`
- Waits for results and prints the first 10 result titles

### `playwright_selectors2.py`
- Uses `playwright.sync_api`
- Navigates to Google News search results for `Generative AI`
- Prints titles and links for the first few articles

## Notes

- `playwright_rpa.py` is the main example for learning basic navigation and form automation.
- If you see import errors, make sure the script is not named `playwright.py` in the same directory and that the correct interpreter is active.
- For headless execution, modify `launch(headless=False)` to `launch(headless=True)`.
