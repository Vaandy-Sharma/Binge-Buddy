import React from "react";
import { Movie } from "../Hooks/useMovies";
import { Box, Heading, Image } from "@chakra-ui/react";

// Props interface for the MovieCard component
interface Props {
  movie: Movie;
  onSelectMovie: (movie: Movie) => void;
}

const MovieCard = ({ movie, onSelectMovie }: Props) => {
  // Function to handle movie selection
  const handleSelectMovie = () => {
    onSelectMovie(movie);
  };

  return (
    <Box
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      cursor="pointer"
      display="flex"
      flexDirection="column"
      alignItems="center"
      onClick={handleSelectMovie}
      backgroundColor="Black"
      color="White"
    >
      
      <Box width="100%" maxHeight="250px" padding="0">
        <Image
          src={movie.movie_poster}
          alt="Movie poster"
          objectFit="fill" 
          width="100%"
          height="100%"
        />
      </Box>
      <Heading as="h2" fontSize="md" marginTop="5">
        {movie.title}
      </Heading>
    </Box>
  );
};

export default MovieCard;
