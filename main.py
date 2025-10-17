from stats import get_book_word_count, char_count, sort_dict

# open a file stream and return it
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
   
    num_chars = char_count(text)
    # print(num_chars)
    res = sort_dict(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for r in res:
        print(f"{r['char']}: {r['num']} ")
    print("============= END ===============")

main()

