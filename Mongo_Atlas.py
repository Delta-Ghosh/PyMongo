import pymongo
import urllib
if __name__ == "__main__":
    print ("Welcome to MongoDB")

client = pymongo.MongoClient("mongodb+srv://ghoshsarthak525_db_user:75**63700@mymongo.asrtlvo.mongodb.net/")
db = client["my_data"]
collection = db["order"]

# inserted = collection.insert_many([
#     {"_id": "1", "name": "John", "address": "Highway 37"},
#     {"_id": "2", "name": "Anna", "address": "Sideway 163"},
#     {"_id": "3", "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": "4", "name": "Linda", "address": "Apple st 652"},
#     {"_id": "5", "name": "James", "address": "Valley 345"},
# ])

dell = collection.delete_many({})
print(dell) #print the delete result