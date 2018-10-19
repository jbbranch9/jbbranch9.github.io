import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #import screen clearing function from os

#initial conditions

word = "bookkeeper" #get word
lng = len(word)

strike = 0

displist = [] #display list of characters representing the word in progress
dispstr = "" #string comprised of current characters in above list
dit = 0 #dit is "display iteration"
new = 0 

while dit < lng:
    displist.append("□")
    dispstr = dispstr+displist[dit]
    dit = dit+1
    
#print(displist)
print(dispstr)

while new < lng and strike < 5:

    print("Guess a letter:")
    ltr = input()

    cls()

    dit = 0
    newbefore = new

    for chk in word:
    
        if chk == ltr:
            displist[dit] = ltr
            new = new+1
        dit = dit+1

    if new != newbefore:

        dispstr = ""

        for rpl in displist:
            dispstr = dispstr+rpl
        
    else:
        strike = strike+1
    
    cls()

    #print(displist)
    print(dispstr)
    print("")
    #print(new)
    print("Strikes")
    print(strike)

cls()

print(dispstr)
print("")

if strike < 5 and new == lng:
    print("You Win!")

else:
    print("Game Over!")
    
input()

