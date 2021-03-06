from random import randint

#import/define screen clearing function
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#defining accepted inputs
R = ["R", "r", "RED", "red", "Red", "R.", "r.", "RED.", "red.", "Red.", "R!", "r!", "RED!", "red!", "Red!"]
G = ["G", "g", "GREEN", "green", "Green", "G.", "g.", "GREEN.", "green.", "Green.", "G!", "g!", "GREEN!", "green!", "Green!"]
B = ["B", "b", "BLUE", "blue", "Blue", "B.", "B.", "BLUE.", "blue.", "Blue.", "B!", "b!", "BLUE!", "blue!", "Blue!"]
W = ["W", "w", "WHITE", "white", "White", "W.", "w.", "WHITE.", "white.", "White.", "W!", "w!", "WHITE!", "white!", "White!"]
P = ["P", "p", "PURPLE", "purple", "Purple", "P.", "p.", "PURPLE.", "purple.", "Purple.", "P!", "p!", "PURPLE!", "purple!", "Purple!"]
O = ["O", "o", "ORANGE", "orange", "Orange", "O.", "o.", "ORANGE.", "orange.", "Orange.", "O!", "o!", "ORANGE!", "orange!", "Orange!"]

#this is what the get_color prompt uses to check that input is valid
def check_input(color_input, color_list, in_list):
    if color_input in color_list:
        in_list = True
        return color_list[0], in_list
    else:
        return color_input, in_list

#prompts player for color
def get_color(prompt):
    in_list = False
    while in_list == False:
        print("Choose a color for peg", prompt)
        color = input("(R=Red, G=Green, B=Blue, or W=White): ")
        print("")
        for i in range(4):
            if in_list == False:
                color, in_list = check_input(color, [R, G, B, W][i], in_list)
        if in_list == False:
            print("Input error. Try again.\n")
    return color

#this generates the code that the players must crack
def generate_code():
    code = []
    for i in range(4):
        index = randint(0,3)
        code.append(["R", "G", "B", "W"][index])
    return code

#using the get_color() prompt, this builds a list of the players 4 guesses
def prompt_player():
    guess = []
    for i in range(4):
        color = get_color(i + 1)
        guess.append(color)
    return guess

"""
This function counts occurrences of each
color within the inputted list and returns
the count in a list of the format:
[# red, # green, # blue, # white]
"""
def color_count(list):
    count_list = []
    for j in range(4):
        color = ["R", "G", "B", "W"][j]
        count = 0
        for i in range(len(list)):
            if list[i] == color:
                count = count + 1
        count_list.append(count)
    return count_list

#checks for color matches between the code and guess lists, returns a number between 0-4
def check_color(code_counts, guess_counts):
    matches = 0
    for i in range(len(code_counts)):
        if code_counts[i] >= guess_counts[i]:
            matches = matches + int(guess_counts[i])
        else:
            matches = matches + int(code_counts[i])
    return int(matches)
        
#returns the number of exact position/color matches, returns a number between 0-4
def check_position(list1, list2):
    matches = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            matches += 1
    return int(matches)

#this clears the screen, and refreshes the list of past guesses each round
def refresh_screen(round, archive):
    cls()
    print("==================Mastermind==================\n", "Round:", round, "/ 10\n")
    if round !=1:
        print("Previous Guesses:\n", "Peg 1===Peg 2===Peg 3===Peg 4===Exact===Color\n")
        display = "  "
        for i in range(int((len(archive)+1)/6)):
            for j in range(6):
                display = display + str(archive[(6*i) + j])
                display = display + "       "
            display = display + "\n  "
        print(display)

def main():
    #initial values
    position_match = 0
    color_match = 0
    round = 1
    code = generate_code()
    guess = ""
    archive = []
    
    """
    The 3 lines below are the "cheat" for debugging.
    They show the "secret code" at the beginning of
    the game if not commented out.
    """
##    cls()
##    print(code)
##    input()
    
    while round <= 10 and guess != code:
        refresh_screen(round, archive)
        
        #prompt player for guess, add guess to archive list
        guess = prompt_player()
        archive.extend(guess)
        
        #check for position/color matches, add them to archive list
        position_match = check_position(code, guess)
        archive.extend(str(position_match))
                
        #check for color only matches, add them to archive list
        #note that the number of position AND color matches is subtracted from the total color matches to get the color ONLY matches
        color_match = check_color(color_count(code), color_count(guess)) - position_match
        archive.extend(str(color_match))
         
        round += 1
    
    #this is the end game procedure
    refresh_screen(round - 1, archive)
    if guess == code:
        print("Congratulations, you cracked the code in", round - 1, "rounds!\n")
    else:
        print("Game over! Better luck next time.\n")
        print("The code was:", code, "\n")
    print("Press 'enter' to replay!")

#call and repeat main() until program is closed
while True:
    main()
    input()
