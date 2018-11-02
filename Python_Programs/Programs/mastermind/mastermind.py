from random import randint

#defining accepted inputs
R = ["R", "r", "RED", "red", "Red", "R.", "r.", "RED.", "red.", "Red.", "R!", "r!", "RED!", "red!", "Red!"]
G = ["G", "g", "GREEN", "green", "Green", "G.", "g.", "GREEN.", "green.", "Green.", "G!", "g!", "GREEN!", "green!", "Green!"]
B = ["B", "b", "BLUE", "blue", "Blue", "B.", "B.", "BLUE.", "blue.", "Blue.", "B!", "b!", "BLUE!", "blue!", "Blue!"]
W = ["W", "w", "WHITE", "white", "White", "W.", "w.", "WHITE.", "white.", "White.", "W!", "w!", "WHITE!", "white!", "White!"]

def get_color(prompt):
    color = ""
    while color != "R" and color != "G" and color != "B" and color != "W":
        print("Choose a color for slot", prompt)
        color = input("(R=Red, G=Green, B=Blue, or W=White): ")
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

def give_feedback():
    return "undefined" 

def main():
    position_match = 0
    color_match = 0
    
    code = generate_code()
    print(code)
    
    print(color_count(code))
    
    guess = prompt_player()
    print(guess)
    
    position_match = check_position(code, guess)
    color_match = check_color(color_count(code), color_count(guess)) - position_match
    
    print("Position and Color:", position_match, "Color Only:", color_match)
    
    




while True:
    main()
    input()