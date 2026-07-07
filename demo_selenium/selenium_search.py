from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Wait for search box
wait = WebDriverWait(driver, 10)

search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Search
search_box.send_keys("Gen AI latest updates")
search_box.send_keys(Keys.RETURN)

# Wait until search results appear
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
)
wait.until(
    EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "div#search h3"))
)

print("=" * 80)
print("Latest Search Results")
print("=" * 80)

# Get first 10 results
results = driver.find_elements(By.CSS_SELECTOR, "div#search h3")

count = 0

for result in results:

    try:
        title = result.text
        link = result.find_element(By.XPATH, "./ancestor::a").get_attribute("href")

        if title:
            count += 1
            print(f"\n{count}. {title}")
            print(link)

        if count == 10:
            break

    except Exception:
        pass

input("\nPress Enter to close browser...")

driver.quit()