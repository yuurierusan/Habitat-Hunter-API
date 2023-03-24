from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import pprint
import os

load_dotenv(find_dotenv())

MONGO_URI = os.environ.get('MONGO_URI')

client = MongoClient(MONGO_URI)
