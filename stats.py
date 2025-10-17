# func that gets the word count from file
def get_book_word_count(book_text):
    return len(book_text.split())

# func that gets the char count from file
def char_count(book_text):
    word_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered not in word_dict:
            word_dict[lowered] = 1
        else:
            word_dict[lowered] += 1
    return word_dict

# func used to sort the char dict
def sort_on(items):
    return items['num']

# func create the list of dicts
def sort_dict(char_dict):
    sorted_list_of_dict = []
    for k in char_dict:
        if k.isalpha():
            sorted_list_of_dict.append({"char": k, "num": char_dict[k]})
    sorted_list_of_dict.sort(reverse=True, key=sort_on)
    return sorted_list_of_dict