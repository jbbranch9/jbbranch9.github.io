import json

with open("data_file.json", "r") as read_file:
    vocabulary = json.load(read_file)
    
for i in [16, 78, 25, 43, 36, 37]:
    print(vocabulary["words'][i])