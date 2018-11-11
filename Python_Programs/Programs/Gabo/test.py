import json
vocabulary = {'stats': {'word count': 2}, 'words': {'0': 'Hello', '1': 'World', "3": "yes"}}
with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
print(vocabulary)
vocabulary['stats']['word count'] = len(vocabulary['words'])
print(vocabulary)