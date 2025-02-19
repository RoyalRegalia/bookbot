def main(): #project variables go here
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    #print(text)
    #print(num_words)
    print(num_characters)

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

