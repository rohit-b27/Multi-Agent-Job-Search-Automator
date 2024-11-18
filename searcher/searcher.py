from tools.scraper_tool import LinkedInScraper
from config import SEARCH_KEYWORDS, SEARCH_LOCATION, EXPERIENCE_LEVEL, LINKEDIN_COOKIE, CHROMEDRIVER_PATH

class SearcherAgent:
    def __init__(self, coordinator):
        self.coordinator = coordinator
        self.scraper = LinkedInScraper(
            SEARCH_KEYWORDS,
            SEARCH_LOCATION,
            EXPERIENCE_LEVEL,
            LINKEDIN_COOKIE,
            CHROMEDRIVER_PATH
        )

    def search_jobs(self):
        self.scraper.login_with_cookie()
        jobs = self.scraper.search_jobs()
        self.scraper.close()
        return jobs
