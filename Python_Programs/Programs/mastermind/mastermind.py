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

def get_color(prompt):
    color = ""
    while color != "R" and color != "G" and color != "B" and color != "W":
        print("Choose a color for peg", prompt)
        color = input("(R=Red, G=Green, B=Blue, or W=White): ")
        print("")
        if color in R:
            color = "R"
        elif color in G:
            color = "G"
        elif color in B:
            color = "B"
        elif color in W:
            color = "W"
        else:
            print("Input error, try typing just the first letter.")
    return color

def generate_code():
    code = []
    for i in range(4):
        x = randint(1,4)
        if x == 1:
            code.append("R")
        elif x == 2:
            code.append("G")
        elif x == 3:
            code.append("B")
        else:
            code.append("W")
    return code

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
    all_colors = ["R", "G", "B", "W"]
    count_list = []
    for j in range(len(all_colors)):
        color = all_colors[j]
        count = 0
        for i in range(len(list)):
            if list[i] == color:
                count = count + 1
        count_list.append(count)
    return count_list

def check_color(code_counts, guess_counts):
    matches = 0
    for i in range(len(code_counts)):
        if code_counts[i] >= guess_counts[i]:
            matches = matches + int(guess_counts[i])
        else:
            matches = matches + int(code_counts[i])
    return int(matches)
        
#returns the number of exact position/color matches
def check_position(list1, list2):
    matches = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            matches += 1
    return int(matches)

def refresh_screen(round, archive):
    cls()
    print("------------------Mastermind------------------")
    print("")
    print("Round:", round + 1)
    print("")

    if round !=0:
        print("Previous Guesses:")
        print("")
        print("Peg 1---Peg 2---Peg 3---Peg 4---Exact---Color")
        print("")
        display = "  "
        for i in range(int((len(archive)+1)/6)):
            for j in range(6):
                display = display + str(archive[(6*i) + j])
                display = display + "       "
            display = display + "\n  "
        print(display)
        print("")

def main():
    position_match = 0
    color_match = 0
    round = 0
    code = generate_code()
    guess = ""
    archive = []
    
    """
    This is the "cheat" for debugging.
    It shows the code at the beginning
    of the game if not commented out.
    cls()
    print(code)
    input()
    """
    
    while round <= 9 and guess != code:
        refresh_screen(round, archive)
                
        guess = prompt_player()
        archive.extend(guess)
        
        position_match = check_position(code, guess)
        archive.extend(str(position_match))
        
        color_match = check_color(color_count(code), color_count(guess)) - position_match
        archive.extend(str(color_match))
         
        round += 1
        
    refresh_screen(9, archive)
    if guess == code:
        print("Congratulations, you cracked the code!")
    else:
        print("Game over! Better luck next time.")
    print("")
    print("Press 'enter' to replay!")

while True:
    main()
    input()