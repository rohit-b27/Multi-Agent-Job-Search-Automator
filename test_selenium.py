from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO)

def test_selenium():
    logging.info("Setting up Chrome options...")
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Specify the path to ChromeDriver
    service = Service("C:/Drivers/chromedriver/chromedriver-win64/chromedriver.exe")

    logging.info("Initializing WebDriver...")
    driver = webdriver.Chrome(service=service, options=options)
    logging.info("Opening Google...")
    driver.get("https://www.google.com")
    logging.info(f"Page title is: {driver.title}")
    driver.quit()
    logging.info("Test completed.")

if __name__ == "__main__":
    test_selenium()
