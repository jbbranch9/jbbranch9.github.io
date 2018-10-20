#import modules
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #import screen clearing function from os

import wordbank #word database, sorted by difficulty

import random

import math

#define funcions
def get_word():
    #setup global variables
    global lvl
    global word
    
    #prompt for difficulty level
    lvl = 0
    while lvl < 1 or lvl > 50:
        #this is to ensure an integer input for difficulty level prompt
        try:
            lvl = int(input("Choose difficulty (1-50): "))
        except ValueError:
            print("Input must be an integer between 1-50.")
    
    #calculate bounds for difficulty level        
    lower_bound = (lvl-1)*85
    upper_bound = 84+lower_bound
    #level 50 has a different upper bound because it has fewer words than the other levels
    if lvl == 50:
        upper_bound = 4234
    
    #word is chosen as a random list index between the upper and lower bounds that define the difficulty level
    index = random.randint(lower_bound, upper_bound)
    word = wordbank.list[index]
 
def startup():
        
    #setup global variables
    global strike
    global max_strike
    global display
    
    #generate "dummy word" as stand-in for word in progress
    display = "□"
    display = display*len(word)
    
    #setup intial values
    strike = 0
    max_strike = 5+math.ceil(lvl*.1)
  
def run_game():
  
    while True:

        letter = input("Guess a letter: ")

        cls()
        
        check_letter(letter)
        
        

#        for chk in word:
#        
#            if chk == ltr:
#                displist[dit] = ltr
#                new = new+1
#            dit = dit+1
#
#        if new != newbefore:
#
#            dispstr = ""
#
#            for rpl in displist:
#                dispstr = dispstr+rpl
#            
#        else:
#            strike = strike+1
#        
#        cls()
#
#        print(dispstr)
#        print("")
#        print("Strikes")
#        print(strike)
#
#        cls()
#
#        print(dispstr)
#        print("")
        
        if strike == max_strike or display == word:
            end_game()

def check_letter(L):
    letter_position = 0
    while letter_position < len(word):
        if L == word[letter_position]:
            display.replace(display[letter_position],L)
        
        

def end_game():

    if display == word:
        print("You Win!")
    else:
        print("Game Over!")

    print(word)
    
    
    
##def run_game():
##  
##    while new < lng and strike < max_strike:
##
##        print("Guess a letter:")
##        ltr = input()
##
##        cls()
##
##        dit = 0
##        newbefore = new
##
##        for chk in word:
##        
##            if chk == ltr:
##                displist[dit] = ltr
##                new = new+1
##            dit = dit+1
##
##        if new != newbefore:
##
##            dispstr = ""
##
##            for rpl in displist:
##                dispstr = dispstr+rpl
##            
##        else:
##            strike = strike+1
##        
##        cls()
##
##        print(dispstr)
##        print("")
##        print("Strikes")
##        print(strike)
##
##    cls()
##
##    print(dispstr)
##    print("")
##
##    if strike < max_strike and dispstr == word:
##        print("You Win!")
##
##    else:
##        print("Game Over!")
##
##    print(word)




while True:
    
    cls()
    get_word()
    startup()
    input()

