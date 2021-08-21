import pymongo
# from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<project_name>.i2omj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.TWFruits
test = db.test



