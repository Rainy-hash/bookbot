import sys
from stats import word_count, char_count, sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = get_book_text(sys.argv[1]) 
    print(book_contents)
    word_count(book_contents)
    char_count(book_contents)
    sorted_dicts(book_contents)
main()

print(sys.argv)