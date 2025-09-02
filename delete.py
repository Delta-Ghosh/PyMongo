import pymongo 

if __name__ == "__main__":
    print("Welcome to MongoDb!")
    print("Data inserted successfully!")
    client = pymongo.MongoClient("mongodb://localhost:27017/") 
    db = client["mydatabase"]
    collection = db["customers"]
    # ONE = collection.delete_one({"name": "John"})  #Delete the first document that matches the query
    ONE = collection.delete_many({})  #Delete all documents in the collection
    print(ONE)
