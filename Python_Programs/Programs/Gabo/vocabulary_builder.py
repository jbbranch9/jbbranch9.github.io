import json
import prime_numbers as prime

vocabulary = {
    "stats": {
        "size": 1
    },
    "words": {
        "001": "Hello",
        "002": "World"
    }
}

prime_number_database = prime.number_list

print(prime_number_database[0])

with open("gabo_vocabulary.json", "w") as write_file:
    json.dump(vocabulary, write_file)