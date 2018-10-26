list = ['b', 'o', 'o', 'k', 'k', 'e', 'e', 'p', 'e', 'r']

def list_to_string(list):
    string = ""
    for x in range(len(list)):
        string = string + list[x]
    return string

string = list_to_string(list)

print(string)
print(string[0:1])