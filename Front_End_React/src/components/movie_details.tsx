import React from "react";
import { Box, Text, Flex, Image, Center } from "@chakra-ui/react";
import { Movie } from "../Hooks/useMovies";

// Props for the MovieDetails component
interface MovieDetailsProps {
  movie: Movie;
}

// MovieDetails component 
const MovieDetails: React.FC<MovieDetailsProps> = ({ movie }) => {
  return (
    <Center>
      <Box p="4" borderWidth="1px" borderRadius="lg" backgroundColor="black" color="white" w="800px">
        <Flex>
          {/* Image on the left side */}
          <Box width="300px" maxHeight="450px" overflow="hidden">
            <Image src={movie.movie_poster} alt={movie.title} width="100%" height="100%" />
          </Box>

          {/* Details on the right side */}
          <Box flex="1" marginLeft="1rem">
            <Text fontWeight="bold" fontSize="25" mb="0">
              {movie.title}
            </Text>
            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Genres:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.genres.join(" ")}
            </Text>

            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Overview:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.overview}
            </Text>

            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Cast:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.cast}
            </Text>

            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Rating:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.average_vote}
            </Text>

            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Director:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.Director}
            </Text>

            <Text fontWeight="bold" fontSize="12" color="blue.500" mb="2">
              Release Date:
            </Text>
            <Text fontSize="12" mb="2">
              {movie.release_date}
            </Text>
          </Box>
        </Flex>
      </Box>
    </Center>
  );
};

export default MovieDetails;
