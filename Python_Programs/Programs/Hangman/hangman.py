#import modules
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #import screen clearing function from os

import word #word database, sorted by difficulty

import random

def get_word():
    #setup global variables
    global lvl
    global word
    
    #prompt for difficulty level
    lvl = 0
    while lvl < 1 or lvl > 50:
    
        lvl = int(input("Choose difficulty (1-50): "))
    
    lower_bound = (lvl-1)*85
    upper_bound = 84+lower_bound
    if lvl == 50:
        upper_bound = 4234
    
    index = random.randint(lower_bound, upper_bound)
    word = word.bank[index]
    
#initial conditions
get_word()

lng = len(word)

strike = 0
if lvl < 26:
    max_strike = 7
else:
    max_strike = 10

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

while new < lng and strike < max_strike:

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

if strike < max_strike and new == lng:
    print("You Win!")

else:
    print("Game Over!")

print(word)

input()
