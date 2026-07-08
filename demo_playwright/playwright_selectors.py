from playwright.sync_api import sync_playwright


def search_genai_news():

    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        # Open Google
        page.goto("https://www.google.com")

        # Wait for search box
        page.wait_for_selector('textarea[name="q"]')

        # Search
        page.fill('textarea[name="q"]', "Gen AI latest updates")

        page.keyboard.press("Enter")

        # Wait for results
        page.wait_for_load_state("networkidle")

        # Print first 10 titles
        print("\nLatest Results\n")

        results = page.locator("h3")

        count = min(results.count(), 10)

        for i in range(count):
            print(f"{i+1}. {results.nth(i).inner_text()}")

        input("\nPress Enter to close browser...")

        browser.close()


if __name__ == "__main__":
    search_genai_news()