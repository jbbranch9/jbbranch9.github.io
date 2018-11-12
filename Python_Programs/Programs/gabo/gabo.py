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
    invalid_words = ["", " "] #list of invalid words. this is a failsafe against the odd word that slips through other filters
    if word not in vocabulary["words"] and word not in invalid_words: #adds new word iff it is not already in list and iff not invalid
        vocabulary["words"].append(word) #this generates a key comprised of "w_" + the next index #
        vocabulary['stats']['word count'] = len(vocabulary['words']) #updates stats: word count += 1

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
    invalid_characters = [",", ".", ":", ";", "!", "?", " "]
    word_list = string_to_list(word)
    for i in word_list:
        if i in invalid_characters:
            word_list.remove(i)
    return list_to_string(word_list)

#returns a list of individual words from a longer string, by identifying and slicing at "whitespace"
def isolate_words(user_prompt):
    word_list = []
    word_break_indices = []
    for i in range(len(user_prompt)): #identifies indices where whitespaces (word breaks) exist
        if user_prompt[i] == " ":
            word_break_indices.append(i)
    word_break_indices.append(len(user_prompt))
    previous_word_break = 0
    for j in word_break_indices: 
        word = strip_non_alpha_numeric(user_prompt[previous_word_break:j]) #defines word as substring between whitespaces (or beginning/end of string), strip out punctuation, etc
        word = word.lower() #makes all words lowercase, thereby making them case-independent for later search algorithm
        word_list.append(word) #builds list of words defined above
        previous_word_break = j
    return word_list

def build_sentence_cipher(words_in_sentence):
    print("")

def identify_phrases(words_in_sentence):
    for i in range(len(words_in_sentence)):
        print("")

def add_sentence_to_vocabulary(vocabulary, sentence, type):
    words_in_sentence = isolate_words(sentence)
    for i in words_in_sentence:
        add_words_to_vocabulary(vocabulary, i)
    
        
def main():
    vocabulary = load_vocabulary()
    prime_number_database = prime.number_list
    
    print(vocabulary)
    
    user_prompt = input("Say something: ")
    add_sentence_to_vocabulary(vocabulary, user_prompt, "user_prompt")
    
    print(vocabulary)
    save_vocabulary(vocabulary)
    
while True:
    main()