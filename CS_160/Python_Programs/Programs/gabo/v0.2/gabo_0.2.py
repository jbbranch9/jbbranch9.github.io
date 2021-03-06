"""
Gabo v0.2
Coded in Python 3.7 by J. Branch

CRITICAL NOTE:
Gabo will only work if the accompanying gabo_vocabulary.json file is in the same folder.

next steps:
    rework accordingly:
        save_session()
        reset_vocabulary()
        end_session()
        save_vocabulary()
    store and recall most_recent_bot as current_bot_name
    find way to pass bot_name from load_bot() to new_bot() that cleanly bypass prompt for new bot_name
        
functions that need work/need to be developed:
    undo_prompt()
    gabo_help()
    
note:
    save_session(), end_session(), and reset_vocabulary()
    are all currently a 'save all'/'reset all'
    options for modifying a single bot are coming later

    print_stats is currently single bot only
    it needs to be reworked into its own function to fix that

planned additions:
    find a way to tag imperative prompts
    integrate parts of speech into metadata and ranking algorithm
    come up with "bot talks first" options
    rank metadata from user prompts and bot responses when selecting best match (not just prompts)
    
changelog since 0.1:
reformatted reset template for vocabulary
reworked vocabulary to be modular, allowing for multiple bots and users to be saved and compartmentalized in the same json file
added new_bot() function
updated print_stats() to account for all bots
added load_bot() function
"""

import json

def reset_template():
    template = {
        'identifiers':
            {
            'bot_name': 'Gabo',
            'user_name': 'User',
            },
        'stats':
            {
            'word count': 1,
            'phrase count': 1,
            'user_prompt count': 1,
            'bot_response count': 1,
             },
        'words':
            [
            'hello',
            ],
        'phrases':
            [
            [0],
            ],
        'user_prompts':
            [
            [['cipher', [0]],
             ['phrases', [0]],
             ['punctuation', [['declarative.', False], ['interrogative?', False], ['exclamatory!', False], ['imperative.!', False]]],
             ['cross ref. ID', 0],
             ['raw string', 'hello']],
            ],
        'bot_responses':
            [
            [['cipher', [0]],
             ['phrases', [0]],
             ['punctuation', [['declarative.', False], ['interrogative?', False], ['exclamatory!', False], ['imperative.!', False]]],
             ['cross ref. ID', 0],
             ['raw string', 'hello']],
            ],
    }
    return template

#loads saved vocabulary database from previous sessions
def load_vocabulary():
    with open("gabo_vocabulary.json", "r") as read_file:
        return json.load(read_file)

#saves vocabulary database for later sessions
def save_vocabulary(vocabulary):
    with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
        
#adds words to vocabulary database, checks for duplicates
def add_words_to_vocabulary(vocabulary, current_bot_name, word):
    invalid_words = ["", " "] #list of invalid words. this is a failsafe against the odd word that slips through other filters
    if word not in vocabulary[current_bot_name]["words"] and word not in invalid_words: #adds new word iff it is not already in list and iff not invalid
        vocabulary[current_bot_name]["words"].append(word) 

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
def build_sentence_cipher(words_in_sentence, vocabulary, current_bot_name):
    cipher = []
    for i in range(len(words_in_sentence)):
        for j in range(len(vocabulary[current_bot_name]["words"])):
            if words_in_sentence[i] == vocabulary[current_bot_name]["words"][j]:
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

def add_phrase_to_vocabulary(vocabulary, current_bot_name, phrase):
    invalid_phrases = [[]] #list of invalid phrases. this is a failsafe against the odd phrase that slips through other filters
    if phrase not in vocabulary[current_bot_name]["phrases"] and phrase not in invalid_phrases: #adds new phrase iff it is not already in list and iff not invalid
        vocabulary[current_bot_name]["phrases"].append(phrase) 

def add_metadata_to_sentence(sentence_cipher, phrases_in_sentence, sentence, vocabulary, current_bot_name):
    sentence_and_metadata = [['cipher', []], ['phrases', []], ['punctuation', []], ['cross ref. ID', []], ['raw string', []]]
    sentence_and_metadata[0][1] = sentence_cipher #adds sentence cipher to sentence metadata
    for i in range(len(phrases_in_sentence)): #adds phrases in sentence to sentence metadata
        for j in range(len(vocabulary[current_bot_name]["phrases"])):
            if phrases_in_sentence[i] == vocabulary[current_bot_name]["phrases"][j]:
                sentence_and_metadata[1][1].append(j)
    sentence_and_metadata[2][1] = tag_punctuation(sentence) #adds tagged punctuation to sentence metadata
    sentence_and_metadata[3][1] = 0
    sentence_and_metadata[4][1] = sentence #adds raw string to sentence metadata
    return sentence_and_metadata

def stat_refresh(vocabulary, current_bot_name):
    vocabulary[current_bot_name]['stats']['word count'] = len(vocabulary[current_bot_name]['words'])
    vocabulary[current_bot_name]['stats']['phrase count'] = len(vocabulary[current_bot_name]['phrases'])
    vocabulary[current_bot_name]['stats']['user_prompt count'] = len(vocabulary[current_bot_name]['user_prompts'])
    vocabulary[current_bot_name]['stats']['bot_response count'] = len(vocabulary[current_bot_name]['bot_responses'])

def add_sentence_to_vocabulary(vocabulary, current_bot_name, sentence, sentence_type):
    words_in_sentence = isolate_words(sentence)
    for i in words_in_sentence:
        add_words_to_vocabulary(vocabulary, current_bot_name, i) #adds words from sentence to vocabulary database
    sentence_cipher = build_sentence_cipher(words_in_sentence, vocabulary, current_bot_name) #builds unique numerical cipher for sentence for faster/easier machine-reading
    phrases_in_sentence = identify_phrases(sentence_cipher)
    for j in phrases_in_sentence:
        add_phrase_to_vocabulary(vocabulary, current_bot_name, j) #adds phrases from sentence to vocabulary database
    sentence_and_metadata = add_metadata_to_sentence(sentence_cipher, phrases_in_sentence, sentence, vocabulary, current_bot_name)
    vocabulary[current_bot_name][sentence_type].append(sentence_and_metadata)
    stat_refresh(vocabulary, current_bot_name)    

def build_matches_list(vocabulary, current_bot_name, prompt_index):
    matches_list = []
    for i in range(prompt_index):
        matches_list.append(0)
    return matches_list

#checks vocabulary for exact match, returns index of match if found, returns -1 if not found
def check_for_exact_matches(vocabulary, current_bot_name, user_prompt):
    exact_match = False
    exact_match_index = 0
    for i in range(len(vocabulary[current_bot_name]['user_prompts'])):
        if user_prompt == vocabulary[current_bot_name]['user_prompts'][i][4][1]:
            exact_match_index = i
            exact_match = True
    return exact_match, exact_match_index

def identify_best_match(ranked_matches):
    for i in range(len(ranked_matches)):
        if ranked_matches[i] == max(ranked_matches):
            best_match = i
    return best_match   

def rank_matches(matches_list, vocabulary, current_bot_name, prompt_index):
    for i in range(prompt_index):
        #adds 1 point for every word in common with the user_prompt
        for j in range(len(vocabulary[current_bot_name]['user_prompts'][prompt_index][0][1])):
            if vocabulary[current_bot_name]['user_prompts'][prompt_index][0][1][j] in vocabulary[current_bot_name]['user_prompts'][i][0][1]:
                matches_list[i] += 1
        #adds 16 points for every punctuation tag in common with the user_prompt
        for k in range(4):
            if vocabulary[current_bot_name]['user_prompts'][prompt_index][2][1][k][1] and vocabulary[current_bot_name]['user_prompts'][i][2][1][k][1]:
                matches_list[i] += 16
        #adds [phrase_length**2] points for every 3- or 5-word phrase in common with the user_prompt
        for l in range(len(vocabulary[current_bot_name]['user_prompts'][prompt_index][1][1])):
            if vocabulary[current_bot_name]['user_prompts'][prompt_index][1][1][l] in vocabulary[current_bot_name]['user_prompts'][i][1][1]:
                matches_list[i] += len(vocabulary[current_bot_name]['phrases'][vocabulary[current_bot_name]['user_prompts'][prompt_index][1][1][l]])**2
    return matches_list

def find_index(vocabulary, current_bot_name, sentence, sentence_type):
    indices = []
    for i in range(len(vocabulary[current_bot_name][sentence_type])):
        if sentence == vocabulary[current_bot_name][sentence_type][i][4][1]:
            indices.append(i)
    return max(indices)

# be aware, that by the time this function is called, the user_prompt has already been added to vocabulary
def respond_to_prompt(vocabulary, current_bot_name, user_prompt, exact_match, exact_match_index):
    if exact_match:
        cross_ref_ID = vocabulary[current_bot_name]['user_prompts'][exact_match_index][3][1]
    else:
        prompt_index = len(vocabulary[current_bot_name]['user_prompts']) - 1 #identifies location of new user_promp in vocabulary
        matches_list = build_matches_list(vocabulary, current_bot_name, prompt_index) #builds a template list for ranking user_prompt matches
        ranked_matches = rank_matches(matches_list, vocabulary, current_bot_name, prompt_index) #ranks all existing user_prompts as potential matches
        best_prompt_match = identify_best_match(ranked_matches) #returns index of best match, given the list generated above
        vocabulary[current_bot_name]['user_prompts'][prompt_index][3][1] = vocabulary[current_bot_name]['user_prompts'][best_prompt_match][3][1] #rewrites the cross-ref ID of the new user_prompt to match that of the "best match"
        cross_ref_ID = vocabulary[current_bot_name]['user_prompts'][prompt_index][3][1] #prints the bot_response string at the index defined by the new cross-red ID
    print("\n", (" "*10), vocabulary[current_bot_name]['identifiers']['bot_name']+":", "\n", (" "*10), vocabulary[current_bot_name]['bot_responses'][cross_ref_ID][4][1], "\n")

def cross_reference_sentences(vocabulary, current_bot_name, user_prompt, corrected_response):
    user_prompt_index = find_index(vocabulary, current_bot_name, user_prompt, 'user_prompts')
    corrected_response_index = find_index(vocabulary, current_bot_name, corrected_response, 'bot_responses')
    vocabulary[current_bot_name]['user_prompts'][user_prompt_index][3][1] = corrected_response_index
    vocabulary[current_bot_name]['bot_responses'][corrected_response_index][3][1] = user_prompt_index

def correct_response(vocabulary, current_bot_name, user_prompt, corrected_response):
    if user_prompt == "/undefined":
        print("\nYou must enter a sentence before correcting a response.\n")
    else:
        if corrected_response == "/undefined":
            print('How should I respond to "', user_prompt, '" ?\n\n')
            corrected_response = input()
        add_sentence_to_vocabulary(vocabulary, current_bot_name, corrected_response, 'bot_responses')
        cross_reference_sentences(vocabulary, current_bot_name, user_prompt, corrected_response)
        print(vocabulary[current_bot_name]['identifiers']['user_name']+":\n", user_prompt, "\n\n", (" "*10), vocabulary[current_bot_name]['identifiers']['bot_name']+":\n", (" "*10), corrected_response, "\n")

####
def undo_prompt():
    print("undo_prompt is not yet developed\n")

#Is there a difference between save_vocabulary() and save_session()?
def save_session(vocabulary):
    save_vocabulary(vocabulary)
    print("\nSaved.\n")
    
def end_session(vocabulary):
    confirm = input("Would you like to save?\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        save_vocabulary(vocabulary)
        print("\nSaved.\n")
    return False
    
def reset_vocabulary(vocabulary):
    confirm = input("Are you sure? This cannot be undone.\nType (Y)es or (N)o:\n")
    if confirm in ["y", "Y", "yes", "YES", "Yes"]:
        vocabulary = {}
        vocabulary['Gabo'] = reset_template()
        save_vocabulary(vocabulary)
        print("\nVocabulary has been reset.\n")
    else:
        print("\nVocabulary has not been reset.\n")
    return vocabulary
    
def auto_save(autosave):
    if autosave:
        print("Auto-save disabled.\n")
    else:
        print("Auto-save enabled.\n")
    return not autosave

def list_commands():
    print('List of user commands:\n\n"/correct" or "//"     = Correct last bot response.\n"/prompt"              = Correct last user prompt.\n"/save"                = Save current session. (Used if autosave it disabled.)\n"/end" or "/exit"      = End session and exit program. (User will be prompted to save.)\n"/reset"               = Resets the vocabulary database to its initial blank slate. (Warning: This cannot be undone.)\n"/print" or "/vocab"   = Print the vocabulary database. (Warning: The database file can get very large, printing may cause crash.)\n"/stats"               = Prints statistics from the vocabulary database.\n"/auto"                = Enable/disable autosave. (Autosave is enabled by default.)\n"/bot"                 = Rename Gabo.\n"/user"                = Rename User.\n"/help" or "/?"        = Get help with Gabo/FAQ.\n"/list" or "/commands" = Print a list of user commands.\n')

####
def gabo_help():
    print("Copy of Gabo README.txt/FAQ\n")
    
def list_bots(vocabulary):
    return [*vocabulary]
    
def check_for_bot(vocabulary, bot_name):
    name_list = list_bots(vocabulary)
    if bot_name in name_list:
        return True
    else:
        return False
    
def new_bot(vocabulary):
    name_in_vocabulary = True
    while name_in_vocabulary:    
        new_bot_name = input("\nWhat is the new bot's name\n")
        name_in_vocabulary = check_for_bot(vocabulary, new_bot_name)
        if name_in_vocabulary:
            print("\nA bot by that name already exists.\n")
    new_user_name = input("\nWhat is the new user's name\n")
    vocabulary[new_bot_name] = reset_template()
    vocabulary[new_bot_name]['identifiers']['bot_name'] = new_bot_name
    vocabulary[new_bot_name]['identifiers']['user_name'] = new_user_name
    return vocabulary, new_bot_name

def print_stats(vocabulary):
    bot_list = list_bots(vocabulary)
    for i in range(len(bot_list)):
        print("Bot Number:", i+1, "\n", vocabulary[bot_list[i]]['identifiers'], "\n", vocabulary[bot_list[i]]['stats'], "\n")
        
def load_bot(vocabulary):
    bot_list = list_bots(vocabulary)
    print("Here are all the bots in the database:\n", bot_list)
    load_successful = False
    while not load_successful:
        bot_to_load = input("\nWhich bot would you like to load?\n")
        if bot_to_load in bot_list:
            load_successful = True
        else:
            print('\nThere is no bot by the name of "', bot_to_load, '"\nWould you like to make a new one?\nType (Y)es or (N)o:\n')
            confirm = input()
            if confirm in ["y", "Y", "yes", "YES", "Yes"]:
                vocabulary, bot_to_load = new_bot(vocabulary)
                load_successful = True
    return vocabulary, bot_to_load
            
                
        

#list of user commands
def commands(user_type_input, running, vocabulary, current_bot_name, autosave, user_prompt):
    print("")
    if user_type_input in ["/correct_response", "/correct response", "/cr", "/CR", "//", "/correct", "/CORRECT", "/Correct"]:
        correct_response(vocabulary, current_bot_name, user_prompt, "/undefined")
    elif user_type_input in ["/undo_prompt", "/undo prompt", "/up", "/UP", "/undo", "/UNDO", "/Undo"]:
        undo_prompt()
    elif user_type_input in ["/save_session", "/save session", "/ss", "/SS", "/save", "/SAVE", "/Save"]:
        save_session(vocabulary)
    elif user_type_input in ["/end_session", "/end session", "/es", "/ES", "/end", "/END", "/End", "/exit", "/EXIT", "/Exit"]:
        running = end_session(vocabulary)
    elif user_type_input in ["/reset_vocabulary", "/reset vocabulary", "/rv", "/RV", "/reset", "/RESET", "/Reset"]:
        vocabulary = reset_vocabulary(vocabulary)
    elif user_type_input in ["/print_vocabulary", "/print vocabulary", "/pv", "/PV", "/vocabulary", "/VOCABULARY", "/Vocabulary", "/vocab", "/VOCAB", "/Vocab", "/print", "/PRINT", "/Print"]:
        print(vocabulary, "\n")
    elif user_type_input in ["/print_stats", "/print stats", "/ps", "/PS", "/stats", "/STATS", "/Stats"]:
        print_stats(vocabulary)
    elif user_type_input in ["/auto_save", "/auto save", "/as", "/AS", "/auto", "/AUTO", "/Auto"]:
        autosave = auto_save(autosave)
    elif user_type_input in ["/gabo_help", "/gabo help", "/help", "/HELP", "/Help", "/readme", "/README", "/Readme", "/?"]:
        gabo_help()
    elif user_type_input in ["/list_commands", "/list commands", "/lc", "/LC", "/list", "/LIST", "/List", "/commands", "/COMMANDS", "/Commands"]:
        list_commands()
    elif user_type_input in ["/rename_bot", "/rename bot", "/rb", "/RB", "/rename", "/RENAME", "/Rename", "/bot", "/BOT", "/Bot"]:
        vocabulary[current_bot_name]['identifiers']['bot_name'] = input("What would you like to name your bot?\n")
    elif user_type_input in ["/rename_user", "/rename user", "/ru", "/RU", "/user", "/USER", "/User"]:
        vocabulary[current_bot_name]['identifiers']['user_name'] = input("What is your name?\n")
    elif user_type_input[0:2] == "//":
        correct_response(vocabulary, current_bot_name, user_prompt, user_type_input[2:])
    elif user_type_input in ["/new_bot", "/new bot", "/nb", "/NB", "/new", "/NEW", "/New"]:
        vocabulary, current_bot_name = new_bot(vocabulary)
    elif user_type_input in ["/load_bot", "/load_bot", "/lb", "/LB", "/load", "/LOAD", "/Load"]:
        vocabulary, current_bot_name = load_bot(vocabulary)
    else:
        print("Command not recognized.\n")
    return user_type_input, running, vocabulary, current_bot_name, autosave 

def welcome_screen():
    print("===================== Welcome to Gabo v0.2 =====================\n")
    print("If you are new to Gabo, please read the README.txt or type /help\n")
    print("Say something...\n")
    
def main():
    vocabulary = load_vocabulary()
    running = True
    autosave = True
    user_prompt = "/undefined"
    current_bot_name = 'Gabo'
    
    welcome_screen()
    
    while running:
        


        user_type_input = input(vocabulary[current_bot_name]['identifiers']['user_name']+":\n")
        if user_type_input[0:1] == "/": #runs commands() function if first character is /
            user_type_input, running, vocabulary, current_bot_name, autosave = commands(user_type_input, running, vocabulary, current_bot_name, autosave, user_prompt)
            
        else:
            user_prompt = user_type_input
            exact_match, exact_match_index = check_for_exact_matches(vocabulary, current_bot_name, user_prompt)
            if not exact_match:
                add_sentence_to_vocabulary(vocabulary, current_bot_name, user_prompt, 'user_prompts')
            respond_to_prompt(vocabulary, current_bot_name, user_prompt, exact_match, exact_match_index)
            
        if autosave:
            save_vocabulary(vocabulary)
            
main()