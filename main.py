import string


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book(book_path)
    print(f"=== Begin report of {book_path}===")
    print(f"word count: {get_count(book_text)}\n")

    char_count = get_chars(book_text)
    sorted_dict = sort_by_count(char_count)

    for k, v in sorted_dict:
        print(f"The '{k}' character was found {v} times")


def get_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_count(text):
    word_list = text.split()
    return len(word_list)


# takes in the book text and returns character count a-c only lowercase
def get_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        elif lowered.isalpha():
            chars[lowered] = 1
    return chars


def sort_by_count(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)


main()
