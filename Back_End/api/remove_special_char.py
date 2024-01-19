#file to remove special characters from the totle field 
import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("modified_movie_dataset_1_with_embeddings.csv")


has_hyphen = df['title'].str.contains(r"-")
df.loc[has_hyphen, 'title'] = df.loc[has_hyphen, 'title'].str.replace(r"-", " ")


has_colon = df['title'].str.contains(r":")
df.loc[has_colon, 'title'] = df.loc[has_colon, 'title'].str.replace(r":", " ")

has_single_quote = df['title'].str.contains(r"'")
df.loc[has_single_quote, 'title'] = df.loc[has_single_quote, 'title'].str.replace(r"'", " ")

has_single_quote = df['title'].str.contains(r".")
df.loc[has_single_quote, 'title'] = df.loc[has_single_quote, 'title'].str.replace(r".", " ")

has_single_quote = df['title'].str.contains(r",")
df.loc[has_single_quote, 'title'] = df.loc[has_single_quote, 'title'].str.replace(r",", " ")

df.to_csv("modified_movie_dataset_with_no_special _charecters.csv", index=False)

print("Hyphens, colons, and single quotes replaced with spaces or removed from the 'title' field in the DataFrame where necessary.")

