from pymongo import MongoClient
import os

MONGO_ID = os.environ['MONGO_ID']
MONGO_PW = os.environ['MONGO_PW']
MONGO_HOST = os.environ['MONGO_HOST']

client = MongoClient('mongodb://'+MONGO_ID+':'+MONGO_PW+'@'+MONGO_HOST, 27017)

mydb = client['test']
mycol = mydb['customers']


def insert_news(news):
    if len(news) > 0:
        mycol.insert_many(news)


def saved_last_date():
    last_row = mycol.find().sort([("createdAt", -1)]).limit(1)
    saved_last = last_row.next()["createdAt"]
    return saved_last
