import pymongo


def getDbConnection(self):
    client = pymongo.MongoClient("mongodb+srv://MyLifeData:<password>@cluster0.dgl0j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.DataLifePy
    return db

