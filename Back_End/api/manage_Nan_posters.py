#file to handle movies with no images and other empty fields

from pymongo import MongoClient
import os

# MongoDB connection setup
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)

db = client['movie_reco_with_embeddings']
collection = db['movies_collection_2']

# Update documents with NaN values in specified fields to empty strings
fields_to_update = ["overview", "genres", "cast", "release_date", "director", "spoken_languages", "embeddings", "movie_poster"]

for field in fields_to_update:
    collection.update_many({field: {"$type": "number"}}, {"$set": {field: ""}})
    collection.update_many({"movie_poster": ""}, {"$set": {"movie_poster": "https://kcil.org.uk/wp-content/uploads/2020/01/awaiting-image-1-e1651572089627.jpg"}})
print("NaN values in the specified fields have been updated to empty strings.")
client.close()

