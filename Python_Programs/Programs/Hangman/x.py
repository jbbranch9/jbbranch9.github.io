global word
word = "bookkeeper"
global display
display = "----------"


def check(L):
    letter_position = 0
    while letter_position < len(word):
        if L == word[letter_position]:
            display.replace(display[letter_position],L)
            letter_position = letter_position + 1
            print(display)

check("o")
print(display)