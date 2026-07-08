from playwright.async_api import async_playwright
import asyncio

async def run_rpa():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        pages = await browser.new_page()

        #navigation to the first page
        await pages.goto("https://www.google.com")
        await pages.wait_for_timeout(10000)  # Wait for 1 second
        await browser.close()

        #Css selector for the search box
        # Step 1: F12 or right click + inspect to open the developer tools
        # Step 2: Element click
        # Step 3: Right click + copy as xpath
        # Step 4: Selectors - copy element

if __name__ == "__main__":
            asyncio.run(run_rpa())