import { useState } from 'react';
import { searchClient } from '../services/api-client';
import { CanceledError } from 'axios';

// Interface to define the shape of a movie
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

// Interface to define the shape of the API response for fetching movies
interface FetchMovieResponse {
  Results: Movie[];
}

// Custom hook to handle searching for movies
const useSearch = () => {
  const [searchMovies, setSearchMovies] = useState<Movie[]>([]);
  const [error, setError] = useState('');

  // Function to handle searching for movies
  const handleSearch = (searchText: string) => {

    // Create an AbortController to manage the request
    const controller = new AbortController();

    // Construct the URL for searching movies
    const url = `/search?title=${encodeURIComponent(searchText)}`;

    // Fetch search results based on the provided search text
    searchClient
      .get<FetchMovieResponse>(url, { signal: controller.signal })
      .then((res) => {
        console.log('Received search results:', res.data.Results);
        console.log('API Response:', res.data);

        // Set the received search results and clear error if results are found
        setSearchMovies(res.data.Results || []);
        setError(res.data.Results && res.data.Results.length > 0 ? '' : 'No movies found');
      })
      .catch((err) => {
        // Handle request cancellation
        if (err instanceof CanceledError) return;
        // Set error message based on the response or a default message
        setError(err.message);
      });
  };

  return { searchMovies, error, handleSearch };
};

export default useSearch;
