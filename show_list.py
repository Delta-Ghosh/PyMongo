import pymongo 

if __name__ == "__main__":
    print("Welcome to MongoDb!")
    print("Data inserted successfully!")

    client = pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)
    db = client["mydatabase"] 
    collection = db["customers"]
    alldatabases = client.list_database_names() #list of databases name
    print(alldatabases) #print the list of databases

    collections = client["mydatabase"] #list of collections name
    print(collections.list_collection_names()) #print the list of collections
