import pymongo 

if __name__ == "__main__":
    print("Welcome to MongoDb!")
    print("Data inserted successfully!")

    client = pymongo.MongoClient("mongodb://localhost:27017/") #Connect to MongoDB server
    print(client)
    db = client["mydatabase"] #Create a database named "mydatabase"
    # collection = db["customers"]
    # ONE = collection.find_one({"name": "John"}) #Find the first document in the collection
    #print(ONE) #Print the first document in the collection
    collection = db["customers"]
    all = collection.find({"name": "John"},{"address": 0}) # address:0 means do not show address field
    for i in all:  
        print(i)    #print(all) #Print the first document in the collection
    # collection = db["customers"]
