def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Returns a dictionary mapping each character to its frequency in the text.
    Characters are converted to lowercase before counting.
    """
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count