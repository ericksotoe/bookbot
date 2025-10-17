from stats import get_book_word_count, char_count, sort_dict
import sys

# open a file stream and return it, this is used to read the books
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # checks to see if the correct number of args is passed in
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # grabs the relative path to the text
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
    num_chars = char_count(text)
    res = sort_dict(num_chars)
    
    # prints out the formatted results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for r in res:
        print(f"{r['char']}: {r['num']} ")
    print("============= END ===============")

main()

