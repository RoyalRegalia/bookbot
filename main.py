def main(): #project variables go here
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    alpha_list = get_list_dict(num_characters)
    alpha_list.sort(reverse = True, key=sort_on)
    report = show_report(book_path,num_words,alpha_list)
    
    #print(text)
    #print(num_words)
    #print(num_characters)

def sort_on(characters):
    return characters['times_found']

def show_report(path,words,characters):
    print (f"--- Begin report of {path} ---")
    print (f"{words} words found in the document")
    
    for char_dict in characters:
        letter = char_dict['char']
        count = char_dict['times_found']
        print (f"The '{letter}' character was found {count} times")

def get_list_dict(char_dict):
    char_dict_list = []
    for char, count in char_dict.items():
        new_dict = {'char': char, 'times_found': count}
        if char.isalpha():
            char_dict_list.append(new_dict)
    return char_dict_list

def get_num_characters(text):
    characters_dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict 
    
def get_num_words(text):
    words = text.split()
    return len(words) #functions must always return some value 
    
def get_book_text(path):
    with open(path) as f: 
        return f.read()

main()

