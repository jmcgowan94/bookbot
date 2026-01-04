import sys
from stats import get_num_words, count_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_string = f.read()
    return file_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book_text = get_book_text(path_to_book)

    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(word_count)

    print("--------- Character Count -------")
    char_count = count_characters(book_text)
    dictionary_sorted = sort_dictionary(char_count)
    for item in dictionary_sorted:
        if not item["name"].isalpha():
            pass
        else:
            print(f"{item['name']}: {item['num']}")
    
    print("============= END ===============")

main()
