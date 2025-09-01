import pymongo 

if __name__ == "__main__":
    print("Welcome to MongoDb!")
    print("Data inserted successfully!")

    client = pymongo.MongoClient("mongodb://localhost:27017/") #Connect to MongoDB server
    print = (client)
    db = client["mydatabase"] #Create a database named "mydatabase"
    collection = db["customers"]
    inserted_data = [
        {"_id":"1","name": "John", "address": "Highway 37"}, #id added to avoid duplicate key error
        {"_id":"2","name": "Anna", "address": "Sideway 163"}, 
        {"_id":"3","name": "Peter", "address": "Lowstreet 27"},
        {"_id":"4","name": "Linda", "address": "Apple st 652"},
        {"_id":"5","name": "James", "address": "Valley 345"},
        {"_id":"6","name": "David", "address": "Ocean blvd 2"},
        {"_id":"7","name": "Susan", "address": "Mountain 21"},
        {"_id":"8","name": "Robert", "address": "Hill st 890"},
        {"_id":"9","name": "Michael", "address": "Canyon 123"},
        {"_id":"10","name": "Jessica", "address": "Sunset 456"}
    ]
    collection.insert_many(inserted_data) #Insert the dictionary into the collection