from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://MyLifeData:DataLifePy@cluster0.dgl0j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.DataLifePy
collection = db.collection.test_collection

post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

collection.insert_one(post);

