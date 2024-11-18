# tools/mongodb_tool.py

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def insert_job(self, job):
        self.collection.insert_one(job)

    def get_all_jobs(self):
        return list(self.collection.find({}))

    def delete_job(self, job_id):
        self.collection.delete_one({"_id": job_id})
