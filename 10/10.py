import requests
import os

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'
NUM_KNOTS = 10


def setup(day):
    if not os.path.exists(day):
        os.mkdir(day)

        with requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies={"session": USER_SESSION_ID}) as response:
                                if response.ok:
                                    data = response.text
                                    input = open(f"{day}"+"/input.txt", "w+")
                                    input.write(data.rstrip("\n"))
                                    input.close()

    data = []
    with open(f"{day}/input.txt", "r") as f:
        line = f.readline()

        while line:
            data.append(line.removesuffix('\n'))
            line = f.readline()
    
    return data


data = setup('10')

CHECK_CYCLES = [20 + 40 * x for x in range(6)]


def parse_command(command):
    if command == 'noop':
        return 'noop', None
    else:
        return command.split(' ')[0], int(command.split(' ')[1])


def part_one():

    CLOCK = 0
    ADDX_CLOCK_CYCLE = 2
    NOOP_CLOCK_CYCLE = 1
    X_VAL = 1

    signals = []

    for line in data:
        command, number = parse_command(line)
        if command == 'addx':
            for i in range(ADDX_CLOCK_CYCLE):
                CLOCK += 1
                if CLOCK in CHECK_CYCLES:
                    signals.append(CLOCK * X_VAL)
            
            X_VAL += number
        else:
            CLOCK += 1
            if CLOCK in CHECK_CYCLES:
                signals.append(CLOCK * X_VAL)

    return sum(signals)


NEWLINE_CYCLES = [39 + 40 * x for x in range(6)]

def print_for_cycle(clock, sprite_position):
    """Print this cycle's char."""
    
    if clock % 40 in sprite_position:
        print('#', end='')
    else:
        print('.', end='')
    
    if clock in NEWLINE_CYCLES:
        print()


def part_two():

    def update_sprite_position(X_VAL):
        return (X_VAL - 1, X_VAL, X_VAL + 1)

    CLOCK = 0
    X_VAL = 1 # sprite center, 3 pixels wide
    sprite_position = (X_VAL - 1, X_VAL, X_VAL + 1)
    ADDX_CLOCK_CYCLE = 2

    for line in data:
        command, number = parse_command(line)
        if command == 'addx':
            for i in range(ADDX_CLOCK_CYCLE):
                print_for_cycle(CLOCK, sprite_position)
                CLOCK += 1
            
            X_VAL += number
            sprite_position = update_sprite_position(X_VAL)
        else:
            print_for_cycle(CLOCK, sprite_position)
            CLOCK += 1

part_two()
