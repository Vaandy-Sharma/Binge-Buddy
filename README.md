# AI-Powered Movie Recommendation Web Application

## Overview
This project is a **content-based movie recommendation web application** that leverages cutting-edge AI techniques to provide highly personalized recommendations based on user search history. The system utilizes word embeddings to encode movie genres and summaries into dense numerical vectors, enabling the model to calculate similarities between movies and user preferences. By computing the shortest distances between these vectors, the application identifies and suggests movies that best match a user’s interests, ensuring highly accurate and individualized recommendations.

## Key Features:
- **Personalized Recommendations**: Tailored movie suggestions based on user search and viewing history.
- **Content-Based Filtering**: Movies are recommended by analyzing the similarity between user preferences and movie content (genres, summaries).
- **Word Embeddings for Text Analysis**: Movie data (e.g., genres and summaries) is converted into dense vectors using OpenAI's text model, allowing for semantic comparison between movies.
- **Efficient Data Management**: The embeddings are pre-generated and stored as a field in the **MongoDB** database, ensuring fast retrieval and response times.
- **Dynamic Front-End**: A user-friendly interface built with **React** for seamless interaction and enhanced user experience.
- **Scalable Backend**: Powered by **Flask**, which manages user requests and interactions with the database efficiently.

## Technical Overview

### Workflow:
1. **Data Processing**:
   - The system retrieves movie details such as genres and summaries.
   - Word embeddings are generated for each movie using OpenAI's text model, encoding the semantic meaning of movie descriptions into dense numerical vectors.
   
2. **Storage**:
   - The generated embeddings are stored in **MongoDB**, facilitating efficient retrieval during recommendation computations.
   
3. **Recommendation Engine**:
   - When a user searches for a movie or provides a history of watched movies, the application calculates the similarity between the user's preferences and the stored movie embeddings by determining the shortest distances between their respective vectors.
   - Based on the similarity scores, movies with the highest relevance to the user are returned as recommendations.
   
4. **User Interface**:
   - A sleek and intuitive **React** front-end provides a seamless user experience, enabling users to browse recommendations, perform searches, and interact with the application effortlessly.

## Core Technologies:
- **Python 3.11.4**: The primary programming language used to build the recommendation engine.
- **Flask 2.3.2**: The web framework responsible for handling backend processes, including user requests and database management.
- **MongoDB**: A NoSQL database used to store and retrieve pre-generated embeddings efficiently, ensuring fast responses.
- **React 18.2.0**: The front-end framework used to build the dynamic, interactive user interface.
- **OpenAI Text Model**: Utilized for generating word embeddings from movie genres and summaries, allowing for advanced semantic text analysis.





