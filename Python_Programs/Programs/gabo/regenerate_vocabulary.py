import json
vocabulary = {'stats': {'size': 2}, 'words': {'1': 'Hello', '2': 'World'}}
with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
print(vocabulary)