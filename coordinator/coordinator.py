# coordinator/coordinator.py

from searcher.searcher import SearcherAgent
from tools.mongodb_tool import MongoDBManager

class CoordinatorAgent:
    def __init__(self):
        # Initialize the SearcherAgent
        self.searcher = SearcherAgent(self)

        # Initialize MongoDB manager to store jobs
        self.db_manager = MongoDBManager()

    def start_process(self):
        print("Starting job search process...")

        # Step 1: Search for jobs
        jobs = self.searcher.search_jobs()
        print(f"Found {len(jobs)} jobs.")

        # Step 2: Save jobs to MongoDB
        for job in jobs:
            self.db_manager.insert_job(job)

        print("Jobs saved to MongoDB.")
