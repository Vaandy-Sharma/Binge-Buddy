import unittest
from app import create_app
from urllib.parse import quote

class TestMovies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the testing environment before running test methods.
        """
         # Use the test configuration for testin

        test_config = {
                       'TESTING': True

        }
        cls.app = create_app(test_config)
        cls.test_client = cls.app.test_client()
        cls.collection = cls.app.database['test_collection']  # Use a test collection for cleaning up
        # Add test data to the test collection
        test_movie_1 = {
            
            "vote_average": 7.6,
            "cast": "Tim Allen|Tom Hanks",
            "director": "Lee Unkrich",
            "genres": [
                "Animation",
                "Family",
                "Comedy"
            ],
            "id": 10193,
            "movie_poster": "https://image.tmdb.org/t/p/original/AbbXspMOwdvwWZgVN0nabZq03Ec.jpg",
            "overview": "Woody, Buzz, and the rest of Andy's toys haven't been played with in years. With Andy about to go to college, the gang find themselves accidentally left at a nefarious day care center. The toys must band together to escape and return home to Andy.",
            "release_date": "16/06/2010",
            "spoken_languages": "['English', 'Español']",
            "title": "Toy Story 3",
            "original_title": "Toy Story 3",

        }
        test_movie_2 = {
                        "vote_average": 6.8,
            "cast": "Guy Pearce|Robert Downey Jr.",
            "director": "Shane Black",
            "genres": [
                "Action",
                "Adventure",
                "Science Fiction"
            ],
            "id": 68721,
            "movie_poster": "https://image.tmdb.org/t/p/original/qhPtAc1TKbMPqNvcdXSOn9Bn7hZ.jpg",
            "overview": "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.",
            "release_date": "18/04/2013",
            "spoken_languages": "['English']",
            "title": "Iron Man 3",
            "original_title": "Iron Man 3"
        }
        test_movie_3={
            "vote_average": 4.4,
            "cast": "Ioan Gruffudd|Michael Chiklis",
            "director": "Tim Story",
            "genres": [
                "Action",
                "Adventure",
                "Science Fiction"
            ],
            "id": 166424,
            "movie_poster": "https://image.tmdb.org/t/p/original/8HLQLILZLhDQWO6JDpvY6XJLH75.jpg",
            "overview": "Four young outsiders teleport to a dangerous universe, which alters their physical form in shocking ways. Their lives irrevocably upended, the team must learn to harness their daunting new abilities and work together to save Earth from a former friend turned enemy.",
            "release_date": "05/08/2015",
            "spoken_languages": "['English']",
            "title": "Fantastic Four",
            "original_title": "Fantastic Four",

            
        }
        test_movie_4={
            "vote_average": 6.0,
            "cast": "Adrien Brody|Laurence Fishburne",
            "director": "Nimród Antal",
            "genres": [
                "Action",
                "Science Fiction",
                "Adventure",
                "Thriller"
            ],
            "id": 34851,
            "movie_poster": "https://image.tmdb.org/t/p/original/wdniP8NDaJIydi1hMxhpbJMUfr6.jpg",
            "overview": "A mercenary reluctantly leads a motley crew of warriors who soon come to realize they've been captured and deposited on an alien planet by an unknown nemesis. With the exception of a peculiar physician, they are all cold-blooded killers, convicts, death squad members... hunters who have now become the hunted.",
            "release_date": "03/07/2010",
            "spoken_languages": "['English', 'Español', 'Pусский']",
            "title": "Predators",
            "original_title": "Predators"
            
        }
        test_movie_5={
            
            "vote_average": 5.8,
            "cast": "",
            "director": "",
            "genres": [
                "Fantasy",
                "Action",
                "Adventure"
            ],
            "id": 849,
            "movie_poster": "https://image.tmdb.org/t/p/original/b1anwwbh00R3iOgM88L5jf7qHBt.jpg",
            "overview": "A prince and a fellowship of companions set out to rescue his bride from a fortress of alien invaders who have arrived on their home planet.",
            "release_date": "29/07/1983",
            "spoken_languages": "['English']",
            "title": "Krull",
            "original_title": "Krull"
            
        }
        test_movie_6={
            
            "vote_average": 5.3,
            "cast": "",
            "director": "",
            "genres": [
                "Action",
                "Fantasy",
                "Science Fiction",
                "Thriller"
            ],
            "id": 16911,
            "movie_poster": "https://kcil.org.uk/wp-content/uploads/2020/01/awaiting-image-1-e1651572089627.jpg",
            "overview": "On the threshold of 22nd century, furrowing the space, protagonist from the Free Search Group makes emergency landing on an unknown planet where he must stay. People who are living on this planet have remained at the stone level of the 20th century, with its social problems, miserable ecology and shaky world..",
            "release_date": "18/12/2008",
            "spoken_languages": "['Pусский']",
            "title": "Obitaemyy Ostrov",
            "original_title": "Obitaemyy Ostrov"
           
        }
        test_movie_7={
            
            "vote_average": 5.8,
            "cast": "",
            "director": "",
            "genres": [
                "Action",
                "Science Fiction",
                "Adventure",
                "Comedy",
                "Family"
            ],
            "id": 88751,
            "movie_poster": "https://image.tmdb.org/t/p/original/myhj05hTAcQL2rhOrMqWxiioo49.jpg",
            "overview": "On a quest to find out what happened to his missing brother, a scientist, his nephew and their mountain guide discover a fantastic and dangerous lost world in the center of the earth.",
            "release_date": "10/07/2008",
            "spoken_languages": "['English', 'Íslenska', 'Italiano']",
            "title": "Journey to the Center of the Earth",
            "original_title": "Journey to the Center of the Earth"
            
        }
        test_movie_8={
            "vote_average": 6.3,
            "cast": "Min-sik Choi|Morgan Freeman|Scarlett Johansson",
            "director": "Luc Besson",
            "genres": [
                "Action",
                "Science Fiction"
            ],
            "id": 240832,
            "movie_poster": "https://image.tmdb.org/t/p/original/kRbpUTRNm6QbLQFPFWUcNC4czEm.jpg",
            "overview": "A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.",
            "release_date": "14/07/2014",
            "spoken_languages": "['普通话', 'English', 'Français', 'Español', '한국어/조선말']",
            "title": "Lucy",
            "original_title": "Lucy"
            
        }
        test_movie_9={
            
            "vote_average": 6.8,
            "cast": "Adrien Brody|Keira Knightley",
            "director": "John Maybury",
            "genres": [
                "Drama",
                "Mystery",
                "Thriller",
                "Fantasy"
            ],
            "id": 9667,
            "movie_poster": "https://image.tmdb.org/t/p/original/etRV2bXIvqqDluok3me7ESnSEij.jpg",
            "overview": "A military veteran goes on a journey into the future, where he can foresee his death and is left with questions that could save his life and those he loves.",
            "release_date": "04/03/2005",
            "spoken_languages": "['English']",
            "title": "The Jacket",
            "original_title": "The Jacket"
            
        }
        test_movie_10={
            "vote_average": 7.2,
            "cast": "Sam Worthington|Sigourney Weaver|Zoe Saldana",
            "director": "James Cameron",
            "genres": [
                "Action",
                "Adventure",
                "Fantasy",
                "Science Fiction"
            ],
            "id": 19995,
            "movie_poster": "https://image.tmdb.org/t/p/original/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg",
            "overview": "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.",
            "release_date": "10/12/2009",
            "spoken_languages": "['English', 'Español']",
            "title": "Avatar",
            "original_title": "Avatar"
            
        }
        test_movie_11={
            "vote_average": 6.8,
            "cast": "Kirsten Dunst|Tobey Maguire",
            "director": "Sam Raimi",
            "genres": [
                "Fantasy",
                "Action"
            ],
            "id": 557,
            "movie_poster": "https://image.tmdb.org/t/p/original/gh4cZbhZxyTbgxQPxD0dOudNPTn.jpg",
            "overview": "After being bitten by a genetically altered spider, nerdy high school student Peter Parker is endowed with amazing powers.",
            "release_date": "01/05/2002",
            "spoken_languages": "['English']",
            "title": "Spider Man",
            "original_title": "Spider-Man", 
        
        }
        
    

        cls.collection.insert_many([test_movie_1, test_movie_2, test_movie_3, test_movie_4, test_movie_5, test_movie_6, test_movie_7, 
                                    test_movie_8, test_movie_9, test_movie_10, test_movie_11])

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the testing environment after all test methods have run.
        """
        
        cls.collection.delete_many({})

    def test_search_movies(self):
        """
        Test the /movies/search endpoint.
        """
        movie_title = 'Spider man'

        response = self.test_client.get(f'/movies/search?title={movie_title}')
        
        data = response.get_json()
       

        self.assertEqual(response.status_code, 200)
        self.assertIn('Results', data)
        self.assertIsInstance(data['Results'], list)
        self.assertEqual(len(data['Results']), 1)

        movie_data = data['Results'][0]
        self.assertEqual(movie_data['title'], 'Spider-Man')
        

    def test_get_all_movies(self):
        """
        Test the /movies endpoint to get a list of all movies.
        """
        response = self.test_client.get('/movies/')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('Movies', data)
        self.assertIsInstance(data['Movies'], list)
        self.assertEqual(len(data['Movies']), 11)

        movie_titles = {movie['title'] for movie in data['Movies']}
        self.assertIn('Toy Story 3', movie_titles)
        self.assertIn('Iron Man 3', movie_titles)

    def test_get_movie_recommendations(self):
        """
        Test the /movies/<movie_title>/recommendations endpoint to get movie recommendations.
        """
        movie_title = 'Avatar'
        encoded_title = quote(movie_title)
        response = self.test_client.get(f'/movies/{encoded_title}/recommendations')
        
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('Recommendations', data)
        self.assertIsInstance(data['Recommendations'], list)

        # Assuming the generate_recommendations function returns movie titles as recommendations
        recommended_movie_titles = {movie['title'] for movie in data['Recommendations']}
        # Add the expected result list
        expected_result = {"Fantastic Four", "Predators", "Krull",  "Journey to the Center of the Earth", "Lucy", "The Jacket"}

        self.assertEqual(recommended_movie_titles, expected_result)

   

if __name__ == '__main__':
    unittest.main()
