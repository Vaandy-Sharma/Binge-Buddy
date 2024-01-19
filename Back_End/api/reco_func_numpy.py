import pymongo
from pymongo import MongoClient
import numpy as np


def generate_recommendations(input_title):
    """
    Generate movie recommendations based on an input movie title.
    """

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017")
    db = client["movie_reco_with_embeddings"]
    collection = db["movies_collection_2"]

    # Retrieve the document with the input title
    document = collection.find_one({"original_title": input_title})
    

    if document:
        # Extract the embeddings field from the retrieved document and parse the string to numpy array
        query_embedding = np.array(document["embedding"])
        
        # Fetch all documents from the collection and parse the embeddings
        all_documents = list(collection.find())
        embedded_arrays = [np.array(doc["embedding"]) for doc in all_documents]
        
        # Calculate distances between the query embedding and other document embeddings
        distances = np.linalg.norm(embedded_arrays - query_embedding, axis=1)
        
        # Sort distances in ascending order and retrieve indices
        sorted_indices = np.argsort(distances)
        

        # Retrieve the twenty nearest neighbors
        nearest_neighbors = [all_documents[i] for i in sorted_indices[:20]]
        

        # Prepare the recommendation results
        recommendations = []
        for neighbor in nearest_neighbors:
            if neighbor['title'] != input_title:
                recommendation = {
                    "title": neighbor['title'],
                    "Distance": distances[sorted_indices.tolist().index(all_documents.index(neighbor))]
                }
                recommendations.append(recommendation)

        # Close the MongoDB connection
        client.close()

        return recommendations

    else:
        # Close the MongoDB connection
        client.close()

        print(f"No document found with title '{input_title}'.")
        return None


