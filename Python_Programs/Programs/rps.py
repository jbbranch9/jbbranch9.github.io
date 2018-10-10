#import/define screen clearing function
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#import random integer function
from random import randint

#import/define print_at function (relocates cursor and/or prints at a specific row/column)
from ctypes import *
 
STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]
 
def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

#initial values
p1_score = 0
p2_score = 0
rps = ["rock", "paper", "scissors"]

#defining accepted inputs
r = ["R", "r", "ROCK", "rock", "Rock", "R.", "r.", "ROCK.", "rock.", "Rock.", "R!", "r!", "ROCK!", "rock!", "Rock!"]
p = ["P", "p", "PAPER", "paper", "Paper", "P.", "p.", "PAPER.", "paper.", "Paper.", "P!", "p!", "PAPER!", "paper!", "Paper!"]
s = ["S", "s", "SCISSORS", "scissors", "Scissors", "S.", "s.", "SCISSORS.", "scissors.", "Scissors.", "S!", "s!", "SCISSORS!", "scissors!", "Scissors!"]

cls()

#title bar
print("---Rock---Paper---Scissors---")
#scoreboard
print("  Player 1:", p1_score, "  Player 2:", p2_score)

#move cursor
print_at(3, 0, "")
print_at(4, 0, "")

#while loop until max score is reached
while True:
    
    #prompt human player input, randomize ai input
    p1 = input("Choose R, P, S:")
    p2 = rps[randint(0,2)]

    #check winner/score
    if p1 in r:
        p1 = "rock"
        if p2 == "scissors":
            p1_score = p1_score + 1
        elif p2 == "paper":
            p2_score = p2_score + 1
    elif p1 in p:
        p1 = "paper"
        if p2 == "rock":
            p1_score = p1_score + 1
        elif p2 == "scissors":
            p2_score = p2_score + 1
    elif p1 in s:
        p1 = "scissors"
        if p2 == "paper":
            p1_score = p1_score + 1
        elif p2 == "rock":
            p2_score = p2_score + 1
            
    cls()

    #title bar
    print("---Rock---Paper---Scissors---")
    #scoreboard
    print("  Player 1:", p1_score, "  Player 2:", p2_score)

    #print r/p/s
    print_at(2, 2, p1)
    print_at(2, 16, p2)
    
    #move cursor
    print_at(3, 0, "")
    print_at(4, 0, "")
    
    #max score/end game, breaks loop
    if p1_score >= 3 or p2_score >= 3:
        break

#declare winner
print("Game Over")
if p1_score > p2_score:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")

input()

