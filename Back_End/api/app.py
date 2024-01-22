#app.py
from flask import Flask
from pymongo import MongoClient
from models import Movie
from flask_cors import CORS
import os



def create_app(test_config:dict = {}):
    '''
    Create Flask application
    '''
    app = Flask(__name__)
    CORS(app)
    
    # Configure MongoDB URI based on the environment variable
    app.config['mongodb_uri'] = os.getenv('MONGODB_URI')

    if len ( test_config)>0:
        # If test configuration is provided, set up a test database
        mongodb_uri = os.getenv('TEST_MONGODB_URI')
        database = MongoClient(mongodb_uri)['test_db']
        collection = database['test_collection']
    
    else:
        # If no test configuration, use default configuration
        mongodb_uri = app.config['mongodb_uri']
        database = MongoClient(mongodb_uri)['movie_reco_with_embeddings']
        collection = database['movies_collection_2']

        # Check if collection exists and add data if not
        if 'movies_collection_2' not in database.list_collection_names():
            Movie.add_data(collection)


    app.database = database
    app.collection = collection

    # Import and register blueprints/routes
    from routes import movies_bp
    app.register_blueprint(movies_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)






