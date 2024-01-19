import openai
import pandas as pd
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

# Import functions and utilities from the OpenAI embeddings module
from openai.embeddings_utils import (
    get_embedding,
    distances_from_embeddings,
    tsne_components_from_embeddings,
    chart_from_components,
    indices_of_nearest_neighbors_from_distances,
)

# Constants for the embedding model and encoding
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base" 


# Read the modified movie dataset from a CSV file
mdf = pd.read_csv('modified_movie_dataset_1.csv')

# Apply the OpenAI's `get_embedding` function to each row in the DataFrame
mdf["embedding"] = mdf.genre_overview_combined.apply(lambda x: get_embedding(x, engine=embedding_model))

# Save the modified DataFrame with embeddings to a new CSV file
mdf.to_csv("modified_movie_dataset_1_with_embeddings.csv")




