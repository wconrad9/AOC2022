import requests
import os
import sys

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

def setup(day):
    if not os.path.exists(day):
        os.mkdir(day)

        with requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies={"session": USER_SESSION_ID}) as response:
                                if response.ok:
                                    data = response.text
                                    input = open(f"{day}"+"/input.txt", "w+")
                                    input.write(data.rstrip("\n"))
                                    input.close()
    
    grid = []
    with open(f"{day}/input.txt", "r") as f:
        line = f.readline()

        while line:
            grid.append(line.removesuffix('\n'))
            line = f.readline()
    
    return grid

grid = setup('8')

GRID_LENGTH = len(grid[0])
GRID_HEIGHT = len(grid)


def check_left(height, i, j):

    if j == -1:
        return True
    if height > int(grid[i][j]):
        return check_left(height, i, j-1)
    else:
        return False


def check_up(height, i, j):

    if i == -1:
        return True
    if height > int(grid[i][j]):
        return check_up(height, i-1, j)
    else:
        return False


def check_right(height, i, j):

    if j == GRID_LENGTH:
        return True
    if height > int(grid[i][j]):
        return check_right(height, i, j+1)
    else:
        return False


def check_down(height, i, j):

    if i == GRID_HEIGHT:
        return True
    if height > int(grid[i][j]):
        return check_down(height, i+1, j)
    else:
        return False


def score_left(height, i, j):

    if j == -1:
        return 0
    if height > int(grid[i][j]):
        return 1 + score_left(height, i, j-1)
    else:
        return 1


def score_up(height, i, j):

    if i == -1:
        return 0
    if height > int(grid[i][j]):
        return 1 + score_up(height, i-1, j)
    else:
        return 1


def score_right(height, i, j):

    if j == GRID_LENGTH:
        return 0
    if height > int(grid[i][j]):
        return 1 + score_right(height, i, j+1)
    else:
        return 1


def score_down(height, i, j):

    if i == GRID_HEIGHT:
        return 0
    if height > int(grid[i][j]):
        return 1 + score_down(height, i+1, j)
    else:
        return 1


def part_one():
    # we have ourselves a 99 x 99 grid
    visible = 0
    for i, row in enumerate(grid):
        for j, tree_height in enumerate(row):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(row) - 1:
                visible += 1
                continue
            
            if check_left(int(tree_height), i, j-1):
                visible+=1
                continue
            if check_up(int(tree_height), i-1, j):
                visible+=1
                continue
            if check_right(int(tree_height), i, j+1):
                visible+=1
                continue
            if check_down(int(tree_height), i+1, j):
                visible+=1
                continue


def part_two():
    # we have ourselves a 99 x 99 grid
    most_scenic = 0
    for i, row in enumerate(grid):
        for j, tree_height in enumerate(row):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(row) - 1:
                continue
            
            left = score_left(int(tree_height), i, j-1)
            up = score_up(int(tree_height), i-1, j)
            right = score_right(int(tree_height), i, j+1)
            down = score_down(int(tree_height), i+1, j)

            score = left * up * right * down
            if score > most_scenic:
                most_scenic = score
    
    return most_scenic


visible = part_one()

most_scenic = part_two()
print(most_scenic)

        