# title = input("Title: ")
# extension = input("Extension: ")

importFile = open("wordlist.txt", "r")
wordList = importFile.readlines()
importFile.close()

print(wordList)

matrix = "("
i = 0

for word in wordList:
    if i == 0:
        matrix += "("
    word = word.replace("\n","")
    matrix += "\'"+word+"\',"

    if i == 999:
        matrix += ")"
        i = 0
        
print(matrix)
    
#print(wordList)

exportFile = open("lexicon_wordset.txt", "w")
exportFile.write(matrix)
exportFile.close()