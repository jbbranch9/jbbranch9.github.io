import json
vocabulary = {'stats': {'size': 2}, 'words': {'0': 'Hello', '1': 'World'}}
with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
print(vocabulary)