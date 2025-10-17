from stats import get_book_word_count, char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
    print(f"Found {num_words} total words")
    num_chars = char_count(text)
    print(num_chars)


main()

