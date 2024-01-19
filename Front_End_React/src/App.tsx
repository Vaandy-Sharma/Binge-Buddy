import { useState, useEffect } from "react";
import { Grid, GridItem, Box, Text, Heading } from "@chakra-ui/react";
import NavBar from "./components/NavBar";
import MovieGrid from "./components/Movie_Grid";
import useSearch, { Movie } from "./Hooks/useSearch";
import useMovies from "./Hooks/useMovies";


function App() {
  const [searchText, setSearchText] = useState("");
  const { searchMovies, error: searchError, handleSearch } = useSearch();
  const { movies: allMovies, error: allMoviesError } = useMovies();
  
  const [selectedMovie, setSelectedMovie] = useState<Movie | null>(null);

  useEffect(() => {
    // Trigger the search when searchText changes
    if (searchText) {
      console.log("Search Text:", searchText);
      handleSearch(searchText); // Call the handleSearch function from the useSearch hook
    }
  }, [searchText]);

  console.log("searchMovies:", searchMovies);
  console.log("allMovies:", allMovies);

  return (
    <Grid
      templateAreas={{
        base: `"nav" "grid1"`,
        md: `"nav nav" "grid1 grid1"`,
        lg: `"nav nav" "grid1 grid1"`,
      }}
      templateColumns={{
        base: "1fr",
        lg: "250px 1fr",
      }}
    >
      <GridItem area="nav">
        {/* Pass a prop to control the visibility of the search bar */}
        <NavBar onSearch={setSearchText} showSearchBar={!selectedMovie} />
      </GridItem>

      {/* Grid 1 */}
      <GridItem area="grid1">
        {/* Conditionally render the "Movie Catalogue" text */}
        {!selectedMovie && (
          <Heading as="h2" size="md" my={4}>
            Movie Catalogue 
          </Heading>
        )}
        <Box height="100%" display="flex" alignItems="center">
          <Text color="white" fontSize="xl" fontWeight="bold" marginLeft="1rem"></Text>
          <MovieGrid
            movies={searchText ? searchMovies : allMovies || []}
            error={searchText ? searchError : allMoviesError}
            onSelectMovie={(movie) => setSelectedMovie(movie)}
            selectedMovie={selectedMovie}
          />
        </Box>
      </GridItem>
    </Grid>
  );
}

export default App;