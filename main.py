from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)

    # Count words
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Count characters
    characters = count_characters(book_text)
    sorted_chars = sort_characters(characters)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

# Execute program
if __name__ == "__main__":
    main()