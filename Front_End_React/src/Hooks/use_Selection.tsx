
import { useState, useEffect } from 'react';
import { searchClient } from '../services/api-client';
import { AxiosRequestConfig, CanceledError } from 'axios';

// Interface for the Movie object
export interface Movie {
  id: number;
  title: string;
  movie_poster: string;
  genres: string[];
  overview:string;
  cast: string;
  Director:string;
  release_date: string;
  average_vote: number;
  similarity?:string

}

// Interface for the response containing recommendations
interface FetchMovieResponse {
  Recommendations: Movie[]; 
}

// Custom hook for fetching movie recommendations based on a selected movie
const useSelection = (selectedMovie: Movie | null, requestConfig?: AxiosRequestConfig) => {
  const [selectedMovies, setSelectedMovies] = useState<Movie[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    if (selectedMovie) {
      const controller = new AbortController();
      const url = `/${encodeURIComponent(selectedMovie.title)}/recommendations`;

       // Fetch recommendations based on the selected movie
      searchClient
        .get<FetchMovieResponse>(url, { signal: controller.signal })
        .then((res) => {
          console.log('Received search results:', res.data.Recommendations); // Update property name
          console.log('API Response:', res.data);

           // Set the received recommendations and clear error if recommendations are found
          setSelectedMovies(res.data.Recommendations || []); 
          setError(res.data.Recommendations && res.data.Recommendations.length > 0 ? '' : 'No recommendations found'); // Update property name
        })
        .catch((err) => {
          // Handle request cancellation
          if (err instanceof CanceledError) return;

          // Set error message based on the response or a default message
          setError(err.response?.data.message || 'An error occurred');
        });
      
        
      return () => {
        controller.abort(); // Cancel the request if the component is unmounted or the selected movie changes
      };
    }
  }, [selectedMovie]);

  return { selectedMovies, error };
};

export default useSelection;
