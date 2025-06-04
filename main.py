from stats import get_num_words, sorted_dictionary_of_chars
from stats import get_characters_appear
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    print('============ BOOKBOT ============')
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

    print("--------- Character Count -------")
    sorted_list_of_char_occurrences = sorted_dictionary_of_chars(get_characters_appear(book_text))
    for char in sorted_list_of_char_occurrences:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()