import { HStack, Spacer, Box, Image, Text } from "@chakra-ui/react";
import logo from '../assets/logo.webp';
import SearchInput from "./search_movie";

// Props interface for the NavBar component
interface Props {
  onSearch: (searchText: string) => void;
  showSearchBar: boolean; // prop to control the visibility of the search bar
}

const NavBar: React.FC<Props> = ({ onSearch, showSearchBar }: Props) => {
  return (
    <HStack>
      <Image src={logo} boxSize="60px" />
      {/* Conditionally render the search bar */}
      {showSearchBar && <SearchInput onSearch={(searchText) => onSearch(searchText)} />}
      <Text fontWeight="bold" whiteSpace='nowrap'>Binge Buddy</Text>
    </HStack>
  );
};

export default NavBar;
