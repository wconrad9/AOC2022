import requests
import os

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

def setup():
    if not os.path.exists("5"):
                os.mkdir("5")

    with requests.get('https://adventofcode.com/2022/day/5/input', cookies={"session": USER_SESSION_ID}) as response:
                            if response.ok:
                                data = response.text
                                input = open("5"+"/input.txt", "w+")
                                input.write(data.rstrip("\n"))
                                input.close()


def get_crates():
    """Let's make an 9 x n dimensional data structure with arrays."""

    crates = [[] for i in range(9)]
    
    with open('5/input.txt') as f:

        row = 1

        while row < 9:

            for col in range(9):

                crate = f.read(3)

                if crate.strip():
                    crates[col].insert(0, crate)
                    f.read(1)
                else:
                    f.read(1)
            
            row += 1
    
    return crates

crates = get_crates()

def move_crate_9000(crates, instruction):
    """Move crates according to the instruction."""

    instruction_list = instruction.split(' ')
    number = int(instruction_list[1])
    src = int(instruction_list[3])
    dest = int(instruction_list[5])

    for i in range(number):

        # remove crate from source
        crate = crates[src-1].pop()

        # add crate to dest
        crates[dest-1].append(crate)
    
    return crates


def move_crate_9001(crates, instruction):
    """Move crates according to the instruction."""

    instruction_list = instruction.split(' ')
    number = int(instruction_list[1])
    src = int(instruction_list[3])
    dest = int(instruction_list[5])

    # create crate stack
    stack = []
    for i in range(number):
        crate = crates[src-1].pop()
        stack.insert(0, crate)

    # add stack to dest
    crates[dest-1] += stack
    
    return crates


def part_one(crates):
    with open('5/input.txt', 'r') as f:
        for i in range(10):
            f.readline()
        instruction = f.readline()

        while instruction:
            crates = move_crate_9000(crates, instruction)
            instruction = f.readline()


def part_two(crates):
    with open('5/input.txt', 'r') as f:
        for i in range(10):
            f.readline()
        instruction = f.readline()

        while instruction:
            crates = move_crate_9001(crates, instruction)
            instruction = f.readline()


def read_crates(crates):

    for i in range(9):
        print(crates[i][len(crates[i])-1][1], end='')


part_two(crates)
read_crates(crates)
