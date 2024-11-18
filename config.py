# config.py
import os
from dotenv import load_dotenv
load_dotenv()
# LinkedIn job search settings
SEARCH_KEYWORDS = "Data Scientist"
SEARCH_LOCATION = "United States"
EXPERIENCE_LEVEL = "Entry Level"

# LinkedIn session cookie (replace with your actual 'li_at' cookie value)
LINKEDIN_COOKIE = os.getenv("LINKEDIN_COOKIE")

# Path to ChromeDriver
CHROMEDRIVER_PATH = "C:/Drivers/chromedriver/chromedriver-win64/chromedriver.exe"  # Update this path if needed

# Database settings (optional, for future use)
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "job_search_db"
COLLECTION_NAME = "job_applications"
