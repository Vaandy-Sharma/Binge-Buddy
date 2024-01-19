import { Input, InputGroup, InputLeftElement } from "@chakra-ui/react";
import { useRef } from 'react';

// Props interface for the SearchInput component
interface Props {
  onSearch: (searchText: string) => void;
}

const SearchInput: React.FC<Props> = ({ onSearch }: Props) => {
  const ref = useRef<HTMLInputElement>(null);
  
  // Handle form submission
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Check if the input value is not empty
    if (ref.current && ref.current.value) {
      onSearch(ref.current.value);
    }
  };

  return (
    // Search form
    <form style={{ width: '100%' }} onSubmit={handleSubmit}>
      <Input
        ref={ref}
        borderRadius={20}
        placeholder="Search movies..."
        variant="filled"
      />
    </form>
  );
};

export default SearchInput;
