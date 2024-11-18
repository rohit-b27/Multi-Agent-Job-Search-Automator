from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class LinkedInScraper:
    def __init__(self, search_keyword, location, experience_level, linkedin_cookie, driver_path):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-webrtc")
        
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)
        self.search_keyword = search_keyword
        self.location = location
        self.experience_level = experience_level
        self.linkedin_cookie = linkedin_cookie

    def login_with_cookie(self):
        # Navigate to LinkedIn to set the cookie
        self.driver.get("https://www.linkedin.com")
        time.sleep(2)  # Ensure the page is fully loaded

        # Add the LinkedIn session cookie
        try:
            self.driver.add_cookie({
                "name": "li_at",
                "value": self.linkedin_cookie,
                "domain": ".linkedin.com"
            })
            print("Cookie added successfully.")
        except Exception as e:
            print("Failed to add cookie:", e)

        # Navigate to LinkedIn Jobs
        self.driver.get("https://www.linkedin.com/jobs/")
        time.sleep(3)

    def search_jobs(self):
        # Ensure the LinkedIn Jobs page is loaded
        self.driver.get("https://www.linkedin.com/jobs/")

        try:
            # Wait for the search input fields to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search jobs')]"))
            )
            search_box = self.driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search jobs')]")
            location_box = self.driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search location')]")

            # Enter search criteria
            search_box.clear()
            search_box.send_keys(self.search_keyword)
            location_box.clear()
            location_box.send_keys(self.location)
            location_box.send_keys("\n")

            # Wait for results to load
            time.sleep(3)
            
            # Debug: Save a screenshot after searching
            # Save screenshot to an absolute path
            screenshot_path = os.path.join(os.getcwd(), "linkedin_debug.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Saved screenshot as {screenshot_path}")
            
            print("Current working directory:", os.getcwd())
            
            jobs = self._scrape_jobs()
            return jobs

        except Exception as e:
            print("Error during job search:", e)
            return []

    def _scrape_jobs(self):
        # Scrape job listings
        jobs = []
        try:
            job_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container"))
            )
            for card in job_cards:
                try:
                    title = card.find_element(By.CLASS_NAME, "job-card-list__title").text
                    company = card.find_element(By.CLASS_NAME, "job-card-container__company-name").text
                    location = card.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
                    link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
                    jobs.append({"title": title, "company": company, "location": location, "link": link})
                except Exception as e:
                    print("Error scraping a job card:", e)

        except Exception as e:
            print("Error scraping job cards:", e)

        return jobs

    def close(self):
        # Quit the browser session
        self.driver.quit()
