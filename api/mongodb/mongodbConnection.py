import pymongo

class mongodbConnection:

    db

    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://MyLifeData:DataLifePy@cluster0.dgl0j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client.DataLifePy

    def getDbConnection(self):
        return self.db

