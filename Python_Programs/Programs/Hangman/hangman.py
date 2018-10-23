#import modules
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear') #import screen clearing function from os

import wordbank #word database, sorted by difficulty

import random

import math


#define functions
def get_word():
 
    #prompt for difficulty level
    L = 0
    while L < 1 or L > 50:
        #this is to ensure an integer input for difficulty level prompt
        try:
            L = int(input("Choose difficulty (1-50): "))
        except ValueError:
            print("Input must be an integer between 1-50.")
    
    #calculate bounds for difficulty level        
    lower_bound = (L-1)*85
    upper_bound = 84+lower_bound
    #level 50 has a different upper bound because it has fewer words than the other levels
    if L == 50:
        upper_bound = 4234
    
    #word is chosen as a random list index between the upper and lower bounds that define the difficulty level
    index = random.randint(lower_bound, upper_bound)
    W = wordbank.list[index]
    
    #return variables
    return W, L

def display():
    cls()
    
    print(wip)


def main():
    
    while True:

        round = 1
        running = True
        
        while running == True:
            get = get_word()
            word = get[0]
            lvl = get[1]
            
            if round == 1:
                strike = 0
            
            max_strike = 5+math.ceil(lvl*.1)
            
            #generate "dummy word" as stand-in for word in progress
            wip = "□"
            wip = wip*len(word)

            
            letter = input("Guess a letter: ")
            


            #cls()
            
            #check(letter, display)

            
            if strike == max_strike or wip == word:
                end_game()



##def check(L,D):
##    letter_position = 0
##    while letter_position < len(word):
##        if L == word[letter_position]:
##            #display.replace(display[letter_position],"X")
##            new_display = D[:letter_position] + "x" + D[(letter_position + 1):]
##        letter_position = letter_position + 1
##    print(new_display)
##    input()
   

def end_game():

    if wip == word:
        print("You Win!")
    else:
        print("Game Over!")
    
    print(word)
    running = False


main()




