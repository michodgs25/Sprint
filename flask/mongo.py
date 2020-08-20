import pymongo
import os
if os.path.exists("env.py"):
  import env

MONGODB_URI = os.environ.get("MONGODB_URI")
# DBS_NAME = os.environ.get("third milestone project")
DBS_NAME = "third_milestone_project"
COLLECTION_NAME = "activities"

def mongo_connect(url):
    # connect to database
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)
# call database and access collection
coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)