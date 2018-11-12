import json
import prime_numbers as prime

def load_vocabulary():
    with open("gabo_vocabulary.json", "r") as read_file:
        return json.load(read_file)

def save_vocabulary(vocabulary):
    with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
        
def add_word_to_vocabulary(vocabulary, word):
    size = vocabulary["stats"]["size"]
    size += 1
    vocabulary["words"][size-1] = word
    vocabulary["stats"]["size"] = size
        
def main():
    vocabulary = load_vocabulary()
    prime_number_database = prime.number_list
    
    print(vocabulary)
    word = input("Word: ")
    add_word_to_vocabulary(vocabulary, word)
    
    print(vocabulary)
    save_vocabulary(vocabulary)
    
while True:
    main()