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

outcomes = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
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
    if opponent_choices[opponent_choice] == my_choices[my_choice]:
        game_points += 3
    
    # my wins
    if my_choice == 'X' and opponent_choice == 'C':
        game_points += 6
    if my_choice == 'Y' and opponent_choice == 'A':
        game_points =+ 6
    if my_choice == 'Z' and opponent_choice == 'B':
        game_points += 6
    
    # add points for shape choice
    if my_choice == 'X':
        game_points += 1
    if my_choice == 'Y':
        game_points += 2
    if my_choice == 'Z':
        game_points += 3
    
    return game_points
    
# part 1
total_points = 0
with open('2/input.txt', 'r') as data:
    
    current_line = data.readline()

    while current_line:
        choices = current_line.split()
        opponent_choice = choices[0]
        my_choice = choices[1]

        total_points += play_rps(opponent_choice, my_choice)

        current_line = data.readline()

print(total_points)


def create_outcome(opponent_choice, outcome):

    # 9 combinations
    # A -> loss draw win
    # B -> loss draw win
    # C -> loss draw win

    if outcome == 'Y':
        return opponent_choices[opponent_choice] + 3
    
    # loss
    if outcome == 'X':
        if opponent_choice == 'A':
            return 3
        if opponent_choice == 'B':
            return 1
        else:
            return 2
    
    if outcome == 'Z':
        if opponent_choice == 'A':
            return 6 + 2
        if opponent_choice == 'B':
            return 6 + 3
        else:
            return 6 + 1


# part 2
new_total_points = 0
with open('2/input.txt', 'r') as data:
    
    current_line = data.readline()

    while current_line:
        choices = current_line.split()
        opponent_choice = choices[0]
        outcome = choices[1]

        new_total_points += create_outcome(opponent_choice, outcome)

        current_line = data.readline()

print("new_total: ", new_total_points)
