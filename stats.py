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

def sort_characters(char_dict):
    """
    Takes a dictionary of characters and counts,
    returns a sorted list of dictionaries in descending order by count.
    Each dictionary: {"char": <character>, "num": <count>}
    """
    sorted_list = []
    for char, num in char_dict.items():
        if char.isalpha():  # skip non-alphabetical characters
            sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list