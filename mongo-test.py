import os
from pprint import pprint
from pymongo import MongoClient

client = MongoClient('')
print("connected to mongo", client)

db = client.researchlytics
print("connected to db", db)

pprint(db.papers.find_one())