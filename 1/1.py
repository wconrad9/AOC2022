import requests
import os

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

if not os.path.exists("2"):
            os.mkdir("2")

with requests.get('https://adventofcode.com/2022/day/2/input', cookies={"session": USER_SESSION_ID}) as response:
                        if response.ok:
                            data = response.text
                            input = open("2"+"/input.txt", "w+")
                            input.write(data.rstrip("\n"))
                            input.close()


opponent_choices = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3  # scissors
}

my_choices = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3  # scissors
}

# line by line, determine result and update score

# 1 point for rock, 2 for paper, 3 for scissors
# 0 points for loss, 3 for draw, 6 for win

# 'X' beats 'C'
# 'Y' beats 'A'
# 'Z' beats 'B'

def play_rps(opponent_choice, my_choice):

    game_points = 0

    # same choice = draw
    if opponent_choice == my_choice:
        game_points += 3
    
    # if I choose rock (X) and they choose scissors (C), I win
    # otherwise 

    if my_choice == 'X' and opponent_choice == 'C':
        game_points += 6
    if my_choice == 'Y' and opponent_choice == 'A':
        game_points =+ 6
    if my_choice == 'Z' and opponent_choice == 'B':
        game_points += 6
    
    return game_points
    

with open('input.txt', 'r') as data:
    
    current_line = data.readline()

    while current_line:
        choices = current_line.split()
        opponent_choice = choices[0]
        my_choice = choices[1]

        current_line = data.readline()
