import json

with open("gabo_vocabulary_dickens.json", "r") as read_file:
    vocabulary = json.load(read_file)

with open("gabo_vocabulary.json", "w") as write_file:
    json.dump(vocabulary, write_file)