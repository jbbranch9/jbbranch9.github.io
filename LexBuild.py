#import text file
importFile = open("wordlist.txt", "r")
#read text into list
wordList = importFile.readlines()
#close to prevent errors
importFile.close()

shelf = []
row = []
book = []


bookIndex = 0
rowIndex = 0
entryIndex = -1

for entry in wordList:
    

    
    entryIndex += 1

    if entryIndex == 0:
        row = []

    #ensure string data type
    entry = str(entry)
    #trim any line breaks    
    entry = entry.replace("\n","")
    #optional all index tag
    entry = str(entryIndex)+"-"+entry
    #add entry (entry) to row list in progress
    row.append(entry)

    



    if entryIndex == 63:
        
        rowArray = tuple(row)

        book.append(rowArray)
        

        entryIndex = -1
        rowIndex += 1



    if rowIndex == 63:

        bookArray = tuple(book)
        print(str(bookIndex)+"-")
        bookIndex+=1
        shelf.append(bookArray)
        book = []
        rowIndex = 0
        print(shelf)
#x = input("pause")
        
           
        

        
        
        


shelfArray = tuple(shelf)
print(shelfArray)


    
    


exportFile = open("lexicon.txt", "w")
exportFile.write(str(shelfArray))
exportFile.close()