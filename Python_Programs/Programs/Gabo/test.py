def string_to_list(string):
    list = []
    for x in string:
        list.append(x)
    return list

def list_to_string(list):
    string = ""
    for x in range(len(list)):
        string = string + list[x]
    return string

def strip_non_alpha_numeric(word):
    invalid_characters = [",", ".", ":", ";", "!", "?"]
    word_list = string_to_list(word)
    for i in word_list:
        if i in invalid_characters:
            word_list.remove(i)
    return list_to_string(word_list)

def isolate_words(user_prompt):
    word_list = []
    word_break_indices = []
    for i in range(len(user_prompt)):
        if user_prompt[i] == " ":
            word_break_indices.append(i)
    word_break_indices.append(len(user_prompt))
    previous_word_break = 0
    for j in word_break_indices:
        word = user_prompt[previous_word_break:j]
        word = strip_non_alpha_numeric(word)
        word_list.append(word)
        previous_word_break = j
    return word_list

isolate_words("The quick, brown fox jumped over the lazy dogs.")

print(strip_non_alpha_numeric("!what,is.this?"))
