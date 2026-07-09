from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)


def search_genai_news():
    news_list = []

    with sync_playwright() as p:

        # Launch browser
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

        # Locate result titles
        results = page.locator("h3")

        count = min(results.count(), 10)

        for i in range(count):
            title = results.nth(i).inner_text()
            news_list.append({
                "rank": i + 1,
                "title": title
            })

        browser.close()

    return news_list


@app.route("/")
def home():
    return "Flask Playwright Application is Running!"


@app.route("/search")
def search():
    news = search_genai_news()

    return jsonify({
        "status": "success",
        "total_results": len(news),
        "news": news
    })


if __name__ == "__main__":
    app.run(debug=True)