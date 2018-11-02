from random import randint

#defining accepted inputs
R = ["R", "r", "RED", "red", "Red", "R.", "r.", "RED.", "red.", "Red.", "R!", "r!", "RED!", "red!", "Red!"]
G = ["G", "g", "GREEN", "green", "Green", "G.", "g.", "GREEN.", "green.", "Green.", "G!", "g!", "GREEN!", "green!", "Green!"]
B = ["B", "b", "BLUE", "blue", "Blue", "B.", "B.", "BLUE.", "blue.", "Blue.", "B!", "b!", "BLUE!", "blue!", "Blue!"]
W = ["W", "w", "WHITE", "white", "White", "W.", "w.", "WHITE.", "white.", "White.", "W!", "w!", "WHITE!", "white!", "White!"]

def get_color():
    color = ""
    while color != "R" and color != "G" and color != "B" and color != "W":
        color = input("Choose a color (R=Red, G=Green, B=Blue, or W=White): ")
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

code = generate_code()
print(code)