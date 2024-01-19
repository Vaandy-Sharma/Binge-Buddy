from flask import Blueprint, jsonify, request, current_app
from models import Movie
from reco_func_numpy import generate_recommendations

# Create a blueprint for movie-related routes
movies_bp = Blueprint('movies', __name__, url_prefix='/movies')


# Route to search for movies based on a query
@movies_bp.route('/search', methods=['GET'])
def search_movies():
    """
    Search for movies based on a query.
    """

    # Get the search query from the request parameters
    query = request.args.get('title')
    collection = current_app.collection

    if query:
        movies = []
        # Find documents with titles that match the query (case-insensitive)
        documents = collection.find({'title': {'$regex': f'{query}', '$options': 'i'}})

        for document in documents:
            # Map the document to a Movie object
            movie = Movie(
                document['original_title'], document['id'], document['overview'], document['genres'], document['cast'],
                document['vote_average'], document['release_date'], document['director'],
                document['spoken_languages'], document['movie_poster']
            )

            movies.append(movie.__dict__)

        if movies:
            return jsonify({'Results': movies})
        else:
             return 'No matching movies found'
    else:
        return 'No search query provided.'
    
    
# Route to get movie recommendations based on a movie title
@movies_bp.route('/<movie_title>/recommendations', methods=['GET'])
def get_movie_recommendations(movie_title):
    
    collection = current_app.collection

    # Find the document with the matching movie_title in the collection
    document = collection.find_one({'original_title': movie_title})

    if document:
        recommendations = generate_recommendations(movie_title)  # Pass movie_title as input_title

        if recommendations:
            reco = []
            for recommendation in recommendations:
                # Find the document with the matching Title in the collection
                document = collection.find_one({'title': recommendation['title']})

                if document:
                    # Map the document to a Movie object
                    movie = Movie(
                        document['original_title'], document['id'], document['overview'], document['genres'],
                        document['cast'], document['vote_average'], document['release_date'],
                        document['director'], document['spoken_languages'], document['movie_poster']
                    )
                    
                    reco.append(movie.__dict__)

            return jsonify({'Recommendations': reco})
        else:
            return 'No recommendations found'
    else:
        return 'Movie not found'
    

# Route to print limited movies from the movies collection
@movies_bp.route('/', methods=['GET'])
def get_all_movies():
    collection = current_app.collection

    # Find all the movies in the collection
    documents = collection.find().limit(30)

    movies = []
    for document in documents:
        # Map the document to a Movie object
        movie = Movie(
            document['original_title'], document['id'], document['overview'], document['genres'], document['cast'],
            document['vote_average'], document['release_date'], document['director'],
            document['spoken_languages'], document['movie_poster']
        )
        movies.append(movie.__dict__)

    if movies:
        return jsonify({'Movies': movies})
    else:
        return 'No movies found'
