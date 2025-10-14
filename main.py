from stats import get_num_of_words, get_num_of_char, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def formatted_print(text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_of_words(text)
    print("--------- Character Count -------")

def print_chardicts(list_of_chars):
    for chardict in list_of_chars:
        print( f"{chardict['char']}: {chardict['num']}")

def main():
    if(len(sys.argv) == 2):
        text = get_book_text(sys.argv[1])

        formatted_print(text)

        char_dict = get_num_of_char(text)
        #print(char_dict)
        list_of_chars = sort_chars(char_dict)
        #print(list_of_chars)
        
        print_chardicts(list_of_chars)
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
main()
