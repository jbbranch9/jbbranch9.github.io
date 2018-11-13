import json
import reset

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
        vocabulary["words"].append(word) 
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

#strips out some, but not all punctuation from a word. leaves apostrophes, accents, hyphens, etc.
def strip_non_alpha_numeric(word):
    invalid_characters = [",", ".", ":", ";", "!", "?", " "]
    word_list = string_to_list(word)
    for i in word_list:
        if i in invalid_characters:
            word_list.remove(i)
    return list_to_string(word_list)

#identifies and lists indices where whitespaces (word breaks) exist
def identify_word_breaks(user_prompt):
    word_break_indices = []
    for i in range(len(user_prompt)): 
        if user_prompt[i] == " ":
            word_break_indices.append(i)
    word_break_indices.append(len(user_prompt))
    return word_break_indices

#returns a list of individual words from a longer string, by identifying and slicing at "whitespace"
def isolate_words(user_prompt):
    word_list = []
    word_break_indices = identify_word_breaks(user_prompt)
    previous_word_break = 0
    for j in word_break_indices: 
        word = strip_non_alpha_numeric(user_prompt[previous_word_break:j]) #defines word as substring between whitespace indices (or beginning/end of string), strips out punctuation, etc
        word = word.lower() #makes all words lowercase, thereby making them case-independent for later search algorithm(s)
        word_list.append(word) #builds list of words defined above
        previous_word_break = j
    return word_list

#builds a cipher for each sentence by saving the index of each word as it is located in the master vocabulary list
def build_sentence_cipher(words_in_sentence, vocabulary):
    cipher = []
    for i in range(len(words_in_sentence)):
        for j in range(len(vocabulary["words"])):
            if words_in_sentence[i] == vocabulary["words"][j]:
                cipher.append(j)
    return cipher

#identifies all "phrases" (sequences of 3 or 5 words) in a sentence
def identify_phrases(sentence_cipher):
    phrase_list = []
    if len(sentence_cipher) <= 3:
        phrase_list.append(sentence_cipher)
    else:
        for i in range(len(sentence_cipher)-2):
            phrase_list.append(sentence_cipher[i:i+3])
        if len(sentence_cipher) >= 5:
            for j in range(len(sentence_cipher)-4):
                phrase_list.append(sentence_cipher[j:j+5])
    return phrase_list

def add_phrase_to_vocabulary(vocabulary, phrase):
    invalid_phrases = [[]] #list of invalid phrases. this is a failsafe against the odd phrase that slips through other filters
    if phrase not in vocabulary["phrases"] and phrase not in invalid_phrases: #adds new phrase iff it is not already in list and iff not invalid
        vocabulary["phrases"].append(phrase) 
        vocabulary['stats']['phrase count'] = len(vocabulary['phrases']) #updates stats: phrase count += 1

def add_sentence_to_vocabulary(vocabulary, sentence, sentence_type):
    words_in_sentence = isolate_words(sentence)
    for i in words_in_sentence:
        add_words_to_vocabulary(vocabulary, i) #adds words from sentence to vocabulary database
    sentence_cipher = build_sentence_cipher(words_in_sentence, vocabulary) #builds unique numerical cipher for sentence for faster/easier machine-reading
    phrases_in_sentence = identify_phrases(sentence_cipher)
    for j in phrases_in_sentence:
        add_phrase_to_vocabulary(vocabulary, j) #adds phrases from sentence to vocabulary database
    if sentence_type == "user_prompt": #sorts by input type
        vocabulary["user_prompts"].append(sentence_cipher)
    elif sentence_type == "bot_response":
        vocabulary["bot_responses"].append(sentence_cipher)
        
def correct_response():
    print("correct response")
    
def correct_prompt():
    print("correct prompt")
    
def save_session(vocabulary):
    save_vocabulary(vocabulary)
    print("Saved.")
    
def end_session():
    confirm = input("Would you like to save?\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        save_vocabulary(vocabulary)
    return False
    
def reset_vocabulary(vocabulary):
    confirm = input("Are you sure? This cannot be undone.\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        from reset import reset_vocabulary
        vocabulary = reset_vocabulary
        save_vocabulary(vocabulary)
        print("Vocabulary has been reset.")
    else:
        print("Vocabulary has not been reset.")
    return vocabulary
    
#def auto_save(auto_save):
#    if auto_save:
#        print("Auto-save disabled.")
#    else:
#        print("Auto-save enabled.")
#    return auto_save

#list of user commands
def commands(user_prompt, running, vocabulary, auto_save):
    if user_prompt in ["/correct_response", "/correct response", "/cr", "/CR", "//"]:
        correct_response()
    elif user_prompt in ["/correct_prompt", "/correct prompt", "/cp", "/CP", "/prompt", "/PROMPT", "/Prompt"]:
        correct_prompt()
    elif user_prompt in ["/save_session", "/save session", "/ss", "/SS", "/save", "/SAVE", "/Save"]:
        save_session(vocabulary)
    elif user_prompt in ["/end_session", "/end session", "/es", "/ES", "/end", "/END", "/End", "/exit", "/EXIT", "/Exit"]:
        running = end_session()
    elif user_prompt in ["/reset_vocabulary", "/reset vocabulary", "/rv", "/RV", "/reset", "/RESET", "/Reset"]:
        vocabulary = reset_vocabulary(vocabulary)
    elif user_prompt in ["/print_vocabulary", "/print vocabulary", "/pv", "/PV", "/vocabulary", "/VOCABULARY", "/Vocabulary", "/vocab", "/VOCAB", "/Vocab", "/print", "/PRINT", "/Print"]:
        print(vocabulary)
    elif user_prompt in ["/auto_save", "/auto save", "/as", "/AS", "/auto", "/AUTO", "/Auto"]:
        if auto_save:
            print("Auto-save disabled.")
        else:
            print("Auto-save enabled.")
        auto_save = not auto_save
    else:
        print("Command not recognized.")
    return user_prompt, running, vocabulary, auto_save 
    
def main():
    vocabulary = load_vocabulary()
    running = True
    auto_save = True
    
    while running:
        
        user_prompt = input("Say something: ")
        if user_prompt[0:1] == "/":
            user_prompt, running, vocabulary, auto_save = commands(user_prompt, running, vocabulary, auto_save)
        else:
            add_sentence_to_vocabulary(vocabulary, user_prompt, "user_prompt")
        
        if auto_save:
            save_vocabulary(vocabulary)
    
main()