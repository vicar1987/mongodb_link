import pymongo
# from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://vicar1987:1ul3u03nji3@twfruit.i2omj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.TWFruits
test = db.test



