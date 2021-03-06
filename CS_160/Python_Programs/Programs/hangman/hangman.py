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
        if L > 50 or L < 1:
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

def display_refresh(wip, strike, max_strike, lvl, letters_guessed, score):
    
    cls()
    
    print("-----------Hangman-----------")
    print("")
    print("Difficulty:", lvl)
    print("Score:", score)
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
    wip_list, correct_letters = search_and_replace(word_list, wip_list, letter)
    wip = list_to_string(wip_list)
    if original_wip == wip:
        new_strike = True
    return wip, new_strike, correct_letters

def string_to_list(string):
    list = []
    for x in string:
        list.append(x)
    return list

def search_and_replace(word_list, wip_list, letter):
    correct_letters = 0
    for x in range(len(word_list)):
        if word_list[x] == letter:
            wip_list[x] = word_list[x]
            correct_letters = correct_letters +1
    return wip_list, correct_letters
            
def list_to_string(list):
    string = ""
    for x in range(len(list)):
        string = string + list[x]
    return string

def assess_strike(strike, letters_guessed, letter):
    strike = strike + 1
    letters_guessed.append(letter)
    return strike, letters_guessed

def assess_score(score, lvl, correct_letters):
    score = score + (lvl * correct_letters)
    return score  

def end_game(wip, word, score):

    if wip == word:
        print("You Win!")
        print("")
        return score

    else:
        print("Game Over!")
        print("")
        print("The word was:", word)
        print("")
        return 0

def main():
    
    score = 0
    
    while True:
        
        #intial values

        strike = 0
        get = get_word()
        word = get[0]
        lvl = int(get[1])
        max_strike = 5+math.ceil(lvl*.1)
        letters_guessed = []
          
        #generate "dummy word" as stand-in for word in progress
        wip = "□"
        wip = wip*len(word)
                 
        while strike < max_strike and wip != word:
            
            display_refresh(wip, strike, max_strike, lvl, letters_guessed, score)

            letter = get_letter()
                 
            wip, new_strike, correct_letters = check(wip, word, letter)

            if (new_strike == True) and (letter not in letters_guessed):
                strike, letters_guessed = assess_strike(strike, letters_guessed, letter)
            else:
                score = assess_score(score, lvl, correct_letters)

        display_refresh(wip, strike, max_strike, lvl, letters_guessed, score)
        score = end_game(wip, word, score)
        print("Press enter to play again.")
        input()
        cls()

main()
