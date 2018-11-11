import json
import prime_numbers as prime

#loads saved vocabulary database from previous sessions
def load_vocabulary():
    with open("gabo_vocabulary.json", "r") as read_file:
        return json.load(read_file)

#saves vocabulary database for later sessions
def save_vocabulary(vocabulary):
    with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
        
#adds words to vocabulary database, checks for duplicates
def add_words_to_vocabulary(vocabulary, word):
    size = vocabulary["stats"]["size"]
    if word not in vocabulary["words"].values():
        size += 1
        vocabulary["words"][size-1] = word
        vocabulary["stats"]["size"] = size

#returns a list comprised of every character in a string, useful because strings are immutable, but lists are not
def string_to_list(string):
    list = []
    for x in string:
        list.append(x)
    return list

#returns a string built from items in a list
def list_to_string(list):
    string = ""
    for x in range(len(list)):
        string = string + list[x]
    return string

#strips out some, but not all punctuation from a word, leaves apostrophes, accents, hyphens, etc.
def strip_non_alpha_numeric(word):
    invalid_characters = [",", ".", ":", ";", "!", "?"]
    word_list = string_to_list(word)
    for i in word_list:
        if i in invalid_characters:
            word_list.remove(i)
    return list_to_string(word_list)

#returns a list of individual words from a longer string, by identifying and slicing at "whitespace"
def isolate_words(user_prompt):
    word_list = []
    word_break_indices = []
    for i in range(len(user_prompt)):
        if user_prompt[i] == " ":
            word_break_indices.append(i)
    word_break_indices.append(len(user_prompt))
    previous_word_break = 0
    for j in word_break_indices:
        word = user_prompt[previous_word_break:j]
        word = strip_non_alpha_numeric(word)
        word_list.append(word)
        previous_word_break = j
    return word_list
        
def main():
    vocabulary = load_vocabulary()
    prime_number_database = prime.number_list
    
    print(vocabulary)
    
    user_prompt = input("Say something: ")
    words_from_prompt = isolate_words(user_prompt)
    for i in words_from_prompt:
        add_words_to_vocabulary(vocabulary, i)
    
    print(vocabulary)
    save_vocabulary(vocabulary)
    
while True:
    main()