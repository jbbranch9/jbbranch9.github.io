def tag_punctuation(sentence_string):
    punctuation_tag = [["declarative.", False], ["interrogative?", False], ["exclamatory!", False], ["imperative.!", False]]
    if "?" in sentence_string:
        punctuation_tag[1][1] = True
    if "!" in sentence_string:
        punctuation_tag[2][1] = True
    if "." in sentence_string and "?" not in sentence_string and "!" not in sentence_string:
        punctuation_tag[0][1] = True
    print(punctuation_tag)
    

tag_punctuation("What?.")
