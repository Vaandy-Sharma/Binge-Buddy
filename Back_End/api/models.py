
import traceback
import ast
import pandas as pd

# Read the CSV file containing movie data with embeddings
movies = pd.read_csv('modified_movie_dataset_1_with_embeddings.csv', low_memory=False)


class Movie:
    def __init__(self, original_title, id, overview, genres, cast, vote_average,release_date,
                  director,spoken_languages, movie_poster):
        
        """
        Initialize a Movie object.
        """
        self.title = original_title
        self.id = id
        self.overview = overview
        self.genres =genres
        self.cast = cast
        self.average_vote = vote_average
        self.release_date = release_date
        self.director = director
        self.spoken_languages=spoken_languages
        self.movie_poster =movie_poster
    
        


    def __repr__(self):

        """
        Return a string representation of the Movie object.
        """
        return f"Movie(original_title='{self.title}', id='{self.id}', overview='{self.overview}', genres='{self.genres}', " \
           f"cast='{self.cast}', average_vote='{self.average_vote}', release_date='{self.release_date}', " \
           f"director='{self.director}', spoken_languages='{self.spoken_languages}', movie_poster='{self.movie_poster}')"

        
    def add_data(collection):
        """
        Add movie data to a database collection.
        """
        try:
            ## Convert columns from array of strings to array of their original datatype
            movies['genres'] = movies['genres'].apply(ast.literal_eval)
            movies['embedding'] = movies['embedding'].apply(ast.literal_eval)

            # Insert data into the collection
            collection.insert_many(movies.to_dict('records'))
            print("Database created")
            return collection
        except Exception as e:
            print("An error occurred while inserting data into the database:")
            traceback.print_exc()
        
    
    


  