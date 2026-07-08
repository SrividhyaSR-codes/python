from playwright.sync_api import sync_playwright


def get_news():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://news.google.com/search?q=Generative%20AI")

        page.wait_for_load_state("networkidle")

        articles = page.locator("article")

        total = min(10, articles.count())

        print("\nLatest GenAI News\n")

        for i in range(total):

            article = articles.nth(i)

            title = article.locator("a").first.inner_text()

            href = article.locator("a").first.get_attribute("href")

            print("-" * 80)
            print(title)
            print(href)

        browser.close()


get_news()