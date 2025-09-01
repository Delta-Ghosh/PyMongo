import pymongo 

if __name__ == "__main__":
    print("Welcome to MongoDb!")
    print("Data inserted successfully!")

    client = pymongo.MongoClient("mongodb://localhost:27017/") #Connect to MongoDB server
    print = (client)
    db = client["mydatabase"] #Create a database named "mydatabase"
    collection = db["customers"] #Create a collection named "customers"
    dictionary = {"name": "John", "address": "Highway 37"} #Create a dictionary to be inserted
    collection.insert_one(dictionary) #Insert the dictionary into the collection



#pip install pymongo first to install pymongo package