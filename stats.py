def get_num_words(book_text):
    book_list = book_text.split()
    word_count = len(book_list)
    return f"Found {word_count} total words"

def count_characters(book_text):
    count_dict = {}

    for char in book_text:
        char = char.lower()
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    dict_list = []
    
    for key, value in dictionary.items():
        entry = {"name": key, "num": value}
        dict_list.append(entry)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list