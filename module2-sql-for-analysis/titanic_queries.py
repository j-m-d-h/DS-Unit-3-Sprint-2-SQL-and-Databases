import pymongo
import pandas as pd


titanic = pd.read_csv('titanic.csv')

data = titanic.to_dict(orient='records')



client = pymongo.MongoClient("mongodb://admin:GC5dObCImlLUa27W@cluster0-shard-00-00-9ecup.mongodb.net:27017,cluster0-shard-00-01-9ecup.mongodb.net:27017,cluster0-shard-00-02-9ecup.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


db.test.insert_many(data)

answer1 = list(db.test.find({"survived": "Yes"}))

print(answer1)
