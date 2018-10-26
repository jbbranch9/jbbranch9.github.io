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
    
    print("-----------Hangman-----------")
    print("")
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

def get_letter():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter = ""
    
    while letter not in alpha:
        letter = input("Guess a letter: ")
        if letter not in alpha:
            print("Input must be a single letter.")
    
    letter = letter.lower()
    return letter

def display_refresh(wip, strike, max_strike, lvl, letters_guessed):
    
    cls()
    
    print("-----------Hangman-----------")
    print("")
    print("Difficulty:", lvl)
    print("Score:")
    print("Strikes:", strike, "/", max_strike)
    print("Letters Guessed:", letters_guessed)
    print("")
    print(wip)
    print("")

def check(wip, word, letter):
    original_wip = wip
    new_strike = False
    word_list = string_to_list(word)
    wip_list = string_to_list(wip)
    wip_list = search_and_replace(word_list, wip_list, letter)
    wip = list_to_string(wip_list)
    if original_wip == wip:
        new_strike = True
    return wip, new_strike

def string_to_list(string):
    list = []
    for x in string:
        list.append(x)
    return list

def search_and_replace(word_list, wip_list, letter):
    for x in range(len(word_list)):
        if word_list[x] == letter:
            wip_list[x] = word_list[x]
    return wip_list
            
def list_to_string(list):
    string = ""
    for x in range(len(list)):
        string = string + list[x]
    return string

def assess_strike(strike, letters_guessed, letter):
    strike = strike + 1
    letters_guessed.append(letter)
    return strike, letters_guessed
    

def end_game(wip, word):

    if wip == word:
        print("You Win!")
    else:
        print("Game Over!")
    
    print(word)
    running = False

def main():
    
    while True:

        loop = 1
        running = True
        
        while running == True:
            
            if loop == 1:
                strike = 0
                get = get_word()
                word = get[0]
                lvl = get[1]
                max_strike = 5+math.ceil(lvl*.1)
                letters_guessed = []
            
                #generate "dummy word" as stand-in for word in progress
                wip = "□"
                wip = wip*len(word)
            
            display_refresh(wip, strike, max_strike, lvl, letters_guessed)

            letter = get_letter()
                 
            wip, new_strike = check(wip, word, letter)

            if (new_strike == True) and (letter not in letters_guessed):
                strike, letters_guessed = assess_strike(strike, letters_guessed, letter)
##            else:
##                assess_score()

            loop = loop + 1
            
            print(strike, wip)
            input()
            
            if strike == max_strike or wip == word:
                #display_refresh(wip, strike, max_strike, lvl) #needed?
                end_game(wip, word)


main()




