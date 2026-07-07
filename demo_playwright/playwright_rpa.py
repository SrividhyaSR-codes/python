from pathlib import Path
from playwright.sync_api import sync_playwright


def run_rpa():
    output_dir = Path(__file__).resolve().parent / "playwright_output"
    output_dir.mkdir(exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(locale="en-US", viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Example automation flow
        page.goto("https://www.google.com")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=output_dir / "example_home.png")

        # Navigate to Wikipedia and perform a search
        page.goto("https://www.wikipedia.org/")
        page.fill("input#searchInput", "Playwright Python")
        page.click("button[type=submit]")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=output_dir / "wikipedia_search.png")

        # Capture a piece of text from the target page
        title = page.locator("h1").first.inner_text()
        print("Captured page title:", title)

        # Example of filling a form on a demo page
        page.goto("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        page.wait_for_load_state("networkidle")
        page.fill("input[name='firstname']", "Vignesh")
        page.fill("input[name='lastname']", "RPA")
        page.fill("input[type='email']", "vignesh@example.com")
        page.fill("textarea[name='msg']", "Automated form submission using Playwright Python.")
        page.screenshot(path=output_dir / "form_filled.png")

        browser.close()


if __name__ == "__main__":
    run_rpa()
