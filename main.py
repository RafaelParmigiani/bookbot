from stats import count_words

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

# Execute program
if __name__ == "__main__":
    main()