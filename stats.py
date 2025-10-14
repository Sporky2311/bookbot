#returns a string with the number of total words in the text provided
def get_num_of_words(text):
    total = len(text.split())
    print(f"Found {total} total words")

#This function returns a dictionary of each letter found in the text provided
def get_num_of_char(text):
    chars = {}
    text = text.lower()
    for letter in text:
        if (letter in chars):
            chars[letter] = chars[letter] + 1
        else:
            chars[letter] = 1
    #for letter in chars:
        #print(f"'{letter}': {chars[letter]},")
    return chars

def sort_on(chars):
    return chars["num"]

def sort_chars(chars):
    dictlist = []
    count = 0
    for char in chars:
        if (char.isalpha()):
            newdict = {"char": char, "num": chars[char]}
            #print(f" {count} and {newdict}")
            dictlist.append(newdict)
    #print(f"This is the dictlist: {dictlist}")
    dictlist.sort(reverse=True, key=sort_on)
    #print(f"This is the sorted dictlist: {dictlist}")
    return dictlist