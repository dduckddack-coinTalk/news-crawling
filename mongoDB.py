from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)

mydb = client['test']
mycol = mydb['customers']


def insert_news(news):
    if len(news) > 0:
        mycol.insert_many(news)


def saved_last_date():
    last_row = mycol.find().sort([("createdAt", -1)]).limit(1)
    saved_last = last_row.next()["createdAt"]
    return saved_last

