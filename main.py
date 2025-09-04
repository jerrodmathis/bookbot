import sys

from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(file_path):
    print(f"Analyzing book found at {file_path}...")
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(path)
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    chars = char_count(text)
    sorted_chars = sort_chars(chars)
    for c in sorted_chars:
        char, num = c["char"], c["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


main()
