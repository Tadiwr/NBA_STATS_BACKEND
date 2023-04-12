from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDB:

    def __init__(self, database:str, collection:str) -> None:
        self.collection_name = collection
        self.database_name = database
        self.uri = "mongodb+srv://tshxng:ShangwA123@nbadatabase.3g1ypoj.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client[self.database_name]
        self.col = self.db[self.collection_name]
        self.test_connection()

    def test_connection(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def insert_one(self, data:dict):
        self.col.insert_one(data)

    def delete_all(self):
        self.col.delete_many({})

    def find_all(self):
        return self.col.find({})
    
    def find(self, query:dict):
        return self.col.find(query)