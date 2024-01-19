import React, { useEffect, useState } from 'react';
import { searchClient } from '../services/api-client';
import { Text } from '@chakra-ui/react';
import { CanceledError } from 'axios';
import ImgSrc from 'react-optimized-image';

// Interface for the Movie object
export interface Movie {
  id: number;
  title: string;
  movie_poster: string;
  genres:string[];
  overview:string;
  cast: string;
  Director:string;
  release_date: string;
  average_vote: number;

}

// Interface for the response containing movie data
interface FetchMovieResponse {
  Movies: Movie[];
 
}
// Custom hook for fetching and managing movie data
const useMovies = () => {
  const [movies, setMovies] = useState<Movie[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    // AbortController to handle request cancellation
    const controller = new AbortController();

    // Fetch movie data from the API endpoint
    searchClient
      .get<FetchMovieResponse>('/', { signal: controller.signal })
      .then((res) => {
        console.log('API Response:', res.data); // Log the full API response
        setMovies(res.data.Movies); // Update the movies state with fetched data
      })
      .catch((err) => {
        if (err instanceof CanceledError) return;
        setError(err.message);
      });

    // Cleanup function to abort the request if the component is unmounted
    return () => controller.abort();
  }, []); //empty array ensures the effect runs only once

   // Log the fetched movies for debugging purposes
  console.log(movies);
  console.log('Movies:', movies);
  
  // Return the fetched movies and error state for external use
  return { movies, error };
};

export default useMovies;
