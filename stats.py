def get_book_word_count(book_text):
    return len(book_text.split())

def char_count(book_text):
    word_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered not in word_dict:
            word_dict[lowered] = 1
        else:
            word_dict[lowered] += 1
    return word_dict
