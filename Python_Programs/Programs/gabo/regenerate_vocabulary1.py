import json
vocabulary = {'stats': {'size': 2}, 'words': ['Hello', 'World']}
with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)
#print(vocabulary)
for i in vocabulary["words"].values():
    print(i)