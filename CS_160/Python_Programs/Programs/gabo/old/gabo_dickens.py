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

def tag_punctuation(sentence_string):
    punctuation_tag = [["declarative.", False], ["interrogative?", False], ["exclamatory!", False], ["imperative.!", False]]
    if "?" in sentence_string:
        punctuation_tag[1][1] = True
    if "!" in sentence_string:
        punctuation_tag[2][1] = True
    if "." in sentence_string and "?" not in sentence_string and "!" not in sentence_string:
        punctuation_tag[0][1] = True
    return punctuation_tag
        
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

def add_metadata_to_sentence(sentence_cipher, phrases_in_sentence, sentence, vocabulary):
    sentence_and_metadata = [['cipher', []], ['phrases', []], ['punctuation', []], ['cross ref. ID', []], ['raw string', []]]
    sentence_and_metadata[0][1] = sentence_cipher #adds sentence cipher to sentence metadata
    for i in range(len(phrases_in_sentence)): #adds phrases in sentence to sentence metadata
        for j in range(len(vocabulary["phrases"])):
            if phrases_in_sentence[i] == vocabulary["phrases"][j]:
                sentence_and_metadata[1][1].append(j)
    sentence_and_metadata[2][1] = tag_punctuation(sentence) #adds tagged punctuation to sentence metadata
    sentence_and_metadata[3][1] = "Response to: " + sentence
    sentence_and_metadata[4][1] = sentence #adds raw string to sentence metadata
    return sentence_and_metadata
 
def add_sentence_to_vocabulary(vocabulary, sentence, sentence_type):
    words_in_sentence = isolate_words(sentence)
    for i in words_in_sentence:
        add_words_to_vocabulary(vocabulary, i) #adds words from sentence to vocabulary database
    sentence_cipher = build_sentence_cipher(words_in_sentence, vocabulary) #builds unique numerical cipher for sentence for faster/easier machine-reading
    phrases_in_sentence = identify_phrases(sentence_cipher)
    for j in phrases_in_sentence:
        add_phrase_to_vocabulary(vocabulary, j) #adds phrases from sentence to vocabulary database
    sentence_and_metadata = add_metadata_to_sentence(sentence_cipher, phrases_in_sentence, sentence, vocabulary)
    vocabulary[sentence_type].append(sentence_and_metadata)

def build_matches_list(vocabulary, prompt_index):
    matches_list = []
    for i in range(prompt_index):
        matches_list.append(0)
    return matches_list

#checks vocabulary for exact match, returns index of match if found, returns -1 if not found
def check_for_exact_matches(vocabulary, user_prompt):
    exact_match = False
    exact_match_index = 0
    for i in range(len(vocabulary['user_prompts'])):
        if user_prompt == vocabulary['user_prompts'][i][4][1]:
            exact_match_index = i
            exact_match = True
    return exact_match, exact_match_index

def rank_matches(matches_list, vocabulary, prompt_index):
    
    for i in range(prompt_index):
        #adds 1 point for every word in common with the user_prompt
        for j in range(len(vocabulary['user_prompts'][prompt_index][0][1])):
            if vocabulary['user_prompts'][prompt_index][0][1][j] in vocabulary['user_prompts'][i][0][1]:
                matches_list[i] += 1
        #adds 16 points for every punctuation tag in common with the user_prompt
        for k in range(4):
            if vocabulary['user_prompts'][prompt_index][2][1][k][1] and vocabulary['user_prompts'][i][2][1][k][1]:
                matches_list[i] += 16
        #adds [phrase_length**2] points for every 3- or 5-word phrase in common with the user_prompt
        for l in range(len(vocabulary['user_prompts'][prompt_index][1][1])):
            if vocabulary['user_prompts'][prompt_index][1][1][l] in vocabulary['user_prompts'][i][1][1]:
                matches_list[i] += len(vocabulary['phrases'][vocabulary['user_prompts'][prompt_index][1][1][l]])**2
    return matches_list

# be aware, that by the time this function is called, the user prompt has already been added to vocabulary
def respond_to_prompt(vocabulary, user_prompt, exact_match, exact_match_index):
    if exact_match:
        print("repond to exact match")
    else:
        prompt_index = len(vocabulary['user_prompts']) - 1
        matches_list = build_matches_list(vocabulary, prompt_index)
        ranked_matches_list = rank_matches(matches_list, vocabulary, prompt_index)
        print(ranked_matches_list)

def stat_refresh(): #needs to be built
    print("stat_refresh needs to be built\n")

def correct_response():
    print("correct response\n")
    
def correct_prompt():
    print("correct prompt\n")
    
def save_session(vocabulary):
    save_vocabulary(vocabulary)
    print("Saved.\n")
    
def end_session(vocabulary):
    confirm = input("Would you like to save?\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        save_vocabulary(vocabulary)
        print("Saved.\n")
    return False
    
def reset_vocabulary(vocabulary):
    confirm = input("Are you sure? This cannot be undone.\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        from reset import reset_vocabulary
        vocabulary = reset_vocabulary
        save_vocabulary(vocabulary)
        print("Vocabulary has been reset.\n")
    else:
        print("Vocabulary has not been reset.\n")
    return vocabulary
    
def auto_save(autosave):
    if autosave:
        print("Auto-save disabled.\n")
    else:
        print("Auto-save enabled.\n")
    return not autosave

def list_commands():
    print('List of user commands:\n\n"/correct" or "//"   = Correct last bot response.\n"/prompt"            = Correct last user prompt.\n"/save"              = Save current session. (Used if autosave it disabled.)\n"/end" or "/exit"    = End session and exit program. (User will be prompted to save.)\n"/reset"             = Resets the vocabulary database to its initial blank slate. (Warning: This cannot be undone.)\n"/print" or "/vocab" = Print the vocabulary database. (Warning: The database file can get very large, printing may cause crash.)\n"/stats"             = Prints statistics from the vocabulary database.\n"/auto"              = Enable/disable autosave. (Autosave is enabled by default.)\n"/help" or "/?"      = Get help with Gabo/FAQ.\n"/list"              = Print a list of user commands.\n')

def gabo_help():
    print("Copy of Gabo README.txt/FAQ\n")

#list of user commands
def commands(user_prompt, running, vocabulary, autosave):
    print("")
    if user_prompt in ["/correct_response", "/correct response", "/cr", "/CR", "//", "/correct", "/CORRECT", "/Correct"]:
        correct_response()
    elif user_prompt in ["/correct_prompt", "/correct prompt", "/cp", "/CP", "/prompt", "/PROMPT", "/Prompt"]:
        correct_prompt()
    elif user_prompt in ["/save_session", "/save session", "/ss", "/SS", "/save", "/SAVE", "/Save"]:
        save_session(vocabulary)
    elif user_prompt in ["/end_session", "/end session", "/es", "/ES", "/end", "/END", "/End", "/exit", "/EXIT", "/Exit"]:
        running = end_session(vocabulary)
    elif user_prompt in ["/reset_vocabulary", "/reset vocabulary", "/rv", "/RV", "/reset", "/RESET", "/Reset"]:
        vocabulary = reset_vocabulary(vocabulary)
    elif user_prompt in ["/print_vocabulary", "/print vocabulary", "/pv", "/PV", "/vocabulary", "/VOCABULARY", "/Vocabulary", "/vocab", "/VOCAB", "/Vocab", "/print", "/PRINT", "/Print"]:
        print(vocabulary, "\n")
    elif user_prompt in ["/print_stats", "/print stats", "/ps", "/PS", "/stats", "/STATS", "/Stats"]:
        print(vocabulary['stats'], "\n")
    elif user_prompt in ["/auto_save", "/auto save", "/as", "/AS", "/auto", "/AUTO", "/Auto"]:
        autosave = auto_save(autosave)
    elif user_prompt in ["/gabo_help", "/gabo help", "/help", "/HELP", "/Help", "/readme", "/README", "/Readme", "/?"]:
        gabo_help()
    elif user_prompt in ["/list_commands", "/list commands", "/lc", "/LC", "/list", "/LIST", "/List"]:
        list_commands()
    else:
        print("Command not recognized.\n")
    return user_prompt, running, vocabulary, autosave 

def welcome_screen():
    print("===================== Welcome to Gabo v0.1 =====================\n")
    print("If you are new to Gabo, please read the README.txt or type /help\n")
    
def main():
    vocabulary = load_vocabulary()
    running = True
    autosave = True
    index = 0
    
    welcome_screen()
    
    while index < 15:
        
        user_prompt = ['Marley was dead: to begin with.', 'There is no doubt whatever about that.', 'The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner.', 'Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to.', 'Old Marley was as dead as a door-nail.', 'Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail.', 'I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade.', 'But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country’s done for.', 'You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail.', 'Scrooge knew he was dead?', 'Of course he did.', 'How could it be otherwise?', 'Scrooge and he were partners for I don’t know how many years.', 'Scrooge was his sole executor, his sole administrator, his sole assign, his sole residuary legatee, his sole friend, and sole mourner.', 'And even Scrooge was not so dreadfully cut up by the sad event, but that he was an excellent man of business on the very day of the funeral, and solemnised it with an undoubted bargain.'][index]
        if user_prompt[0:1] == "/":
            user_prompt, running, vocabulary, autosave = commands(user_prompt, running, vocabulary, autosave)
        else:
            exact_match, exact_match_index = check_for_exact_matches(vocabulary, user_prompt)
            if not exact_match:
                add_sentence_to_vocabulary(vocabulary, user_prompt, 'user_prompts')
            respond_to_prompt(vocabulary, user_prompt, exact_match, exact_match_index)
        
        if autosave:
            save_vocabulary(vocabulary)
            
        index += 1    
main()