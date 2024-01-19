
import { Box, SimpleGrid, Text, Heading } from '@chakra-ui/react';
import { Movie } from '../Hooks/useMovies';
import MovieCard from './MovieCard';
import useSelection from "../Hooks/use_Selection";
import MovieDetails from './movie_details'; 

// the props interface for MovieGrid component
interface MovieGridProps {
  movies: Movie[];
  error: string;
  onSelectMovie: (movie: Movie) => void;
  selectedMovie: Movie | null;
}

// MovieGrid component 
const MovieGrid: React.FC<MovieGridProps> = ({ movies, error, onSelectMovie, selectedMovie }) => {
  const { selectedMovies, error: selectError } = useSelection(selectedMovie);
  
  // If a movie is selected, its details and recommendations are displayed

  if (selectedMovie) {
    return (
      <Box>
        <MovieDetails movie={selectedMovie} />
        
        {/* recommendations heading */}
        <Heading as="h2" size="md" my={4}>
          Recommendations
        </Heading>

        {/* An error message is displayed if there's a selection error */}
        {selectError && <Text>{selectError}</Text>}

        {/* responsive grid for the selected movies */}
        <SimpleGrid columns={{ base: 1, sm: 2, md: 3, lg: 5, xl: 6 }} spacing={5}>
          {selectedMovies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} onSelectMovie={onSelectMovie} />
          ))}
        </SimpleGrid>
      </Box>
    );
  }
  // If no movie is selected, regular movie grid is displayed
  return (
    <Box>
      {error && <Text>{error}</Text>}
      
      {/* Responsive grid for the selected movies */}
      <SimpleGrid columns={{ base: 1, sm: 2, md: 3, lg: 5, xl: 6 }} spacing={5}>
        {movies.map((movie) => (
          <MovieCard key={movie.id} movie={movie} onSelectMovie={onSelectMovie} />
        ))}
      </SimpleGrid>
    </Box>
  );
};

export default MovieGrid;
