import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def scrape_website(website):
    chrome_driver_path = "/home/pranav/Downloads/chromedriver-linux64/chromedriver"

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment if you don't need a GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = None
    html = ''

    try:
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        driver.get(website)

        # Use explicit wait to ensure page is loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        html = driver.page_source

    except Exception as e:
        print(f"An error occurred while scraping: {e}")

    finally:
        if driver:
            driver.quit()

    return html


def clean_html(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    body = soup.body
    return str(body) if body else ''


def clean_body_text(body):
    soup = BeautifulSoup(body, 'html.parser')

    # Remove script and style tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()  # .decompose() is efficient for removal

    # Extract and clean text
    cleaned = soup.get_text(separator="\n")
    cleaned = "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())

    return cleaned


def create_chunks(text_content, max_limit=6000):
    return [text_content[i: i + max_limit] for i in range(0, len(text_content), max_limit)]


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Website"
    html = scrape_website(url)
    cleaned_html = clean_html(html)
    cleaned_body_text = clean_body_text(cleaned_html)
    chunked_data = create_chunks(cleaned_body_text)

    print(chunked_data)
