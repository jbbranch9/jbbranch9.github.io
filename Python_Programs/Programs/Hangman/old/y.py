def search_and_replace(word_list, letter):
    for x in range(len(word_list)):
        if word_list[x] == letter:
            wip_list[x] = word_list[x]
    return wip_list
            
def string_to_list(string):
    list = []
    for x in string:
        list.append(x)
    return list

word_list = string_to_list("bookkeeper")
wip_list = string_to_list("-oo-------")
letter = "e"

print(search_and_replace(word_list, wip_list, letter))
