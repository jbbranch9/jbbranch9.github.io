#import/define screen clearing function
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#import random integer function
import random

def format_player_1_input(rock_list, paper_list, scissors_list, player_1_input):
    if player_1_input in rock_list:
        return "rock"
    elif player_1_input in paper_list:
        return "paper"
    elif player_1_input in scissors_list:
        return "scissors"

def get_player_1_input(rock_list, paper_list, scissors_list):
    valid_inputs = rock_list + paper_list + scissors_list
    player_1_input = ""
    while player_1_input not in valid_inputs:
        player_1_input = input("\nChoose R, P, S:\n")
        if player_1_input not in valid_inputs:
            print("\nInvalid input. Try again.")
    formatted_player_1_input = format_player_1_input(rock_list, paper_list, scissors_list, player_1_input)
    return formatted_player_1_input
            
def score_round(player_1_input, player_2_input, p1_score, p2_score):
    if player_1_input == "rock":
        if player_2_input == "scissors":
            p1_score = p1_score + 1
        elif player_2_input == "paper":
            p2_score = p2_score + 1
    elif player_1_input == "paper":
        if player_2_input == "rock":
            p1_score = p1_score + 1
        elif player_2_input == "scissors":
            p2_score = p2_score + 1
    elif player_1_input == "scissors":
        if player_2_input == "paper":
            p1_score = p1_score + 1
        elif player_2_input == "rock":
            p2_score = p2_score + 1
    return p1_score, p2_score

def main():
    while True:
        #initial values
        p1_score = 0
        p2_score = 0
        player_1_input = ""
        player_2_input = ""

        #defining accepted inputs
        rock_list = ["R", "r", "ROCK", "rock", "Rock", "R.", "r.", "ROCK.", "rock.", "Rock.", "R!", "r!", "ROCK!", "rock!", "Rock!"]
        paper_list = ["P", "p", "PAPER", "paper", "Paper", "P.", "p.", "PAPER.", "paper.", "Paper.", "P!", "p!", "PAPER!", "paper!", "Paper!"]
        scissors_list = ["S", "s", "SCISSORS", "scissors", "Scissors", "S.", "s.", "SCISSORS.", "scissors.", "Scissors.", "S!", "s!", "SCISSORS!", "scissors!", "Scissors!"]

        while p1_score < 3 and p2_score < 3:
            
            cls()
            
            #title bar, scorecard, and round results
            print("======Rock=====Paper=====Scissors=====\n\nPlayer 1 Score:", p1_score, "  Player 2 Score:", p2_score, "\n\nPlayer 1:", player_1_input, " "*(8-len(player_1_input)), "Player 2:", player_2_input)
        
            player_1_input = get_player_1_input(rock_list, paper_list, scissors_list)
            player_2_input = random.choice(["rock", "paper", "scissors"])
            p1_score, p2_score = score_round(player_1_input, player_2_input, p1_score, p2_score)
            
        #declare winner
        cls()
        print("======Rock=====Paper=====Scissors=====\n\nPlayer 1 Score:", p1_score, "  Player 2 Score:", p2_score, "\n\nPlayer 1:", player_1_input, " "*(8-len(player_1_input)), "Player 2:", player_2_input, "\n\nGame Over")
        if p1_score > p2_score:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
        input("\nPress enter to play again.")

main()