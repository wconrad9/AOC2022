import requests
import os
import math

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


data = setup('9')

tail_locations = set() # for part 2
tail_locations.add((0,0)) # for part 2


class Tail():

    def __init__(self):
        self.x, self.y = 0,0
    
    def move_tail(self, direction, head_x, head_y):
        """Move the tail according to the head pos."""
        
        # cardinal move
        if self.x == head_x or self.y == head_y:
            if direction == 'U':
                self.y += 1
                return
            if direction == 'R':
                self.x += 1
                return
            if direction == 'D':
                self.y -= 1
                return
            if direction == 'L':
                self.x -= 1
                return
        # diagonal move
        else:
            # diagonal up right
            if direction == 'U' and self.x < head_x:
                self.y += 1
                self.x += 1
                return
            # diagonal up left
            if direction == 'U' and self.x > head_x:
                self.y += 1
                self.x -= 1
                return
            # diagonal right up
            if direction == 'R' and self.y < head_y:
                self.x += 1
                self.y += 1
                return
            # diagonal right down
            if direction == 'R' and self.y > head_y:
                self.x += 1
                self.y -= 1
                return
            # diagonal down right
            if direction == 'D' and self.x < head_x:
                self.y -= 1
                self.x += 1
                return
            # diagonal down left
            if direction == 'D' and self.x > head_x:
                self.y -= 1
                self.x -= 1
                return
            # diagonal left up
            if direction == 'L' and self.y < head_y:
                self.x -= 1
                self.y += 1
                return
            # diagonal left down
            if direction == 'L' and self.y > head_y:
                self.x -= 1
                self.y -= 1
                return


class Knot():

    def __init__(self, num_knots_remaining):
        self.x, self.y = 0,0
        self.tail = False
        if num_knots_remaining == 1:
            self.tail = True
            self.next: Knot = None
            return
        self.next: Knot = Knot(num_knots_remaining-1)

    
    def next_is_distant(self):
        """Return True if tail > 1 space from head, False if not."""
        if abs(self.x - self.next.x) > 1 or abs(self.y - self.next.y) > 1:
            return True
        else:
            return False
    

    def determine_direction(self, prev_x, prev_y):
        if prev_x > self.x and prev_y == self.y:
            return "R"
        if prev_x == self.x and prev_y > self.y:
            return "U"
        if prev_x < self.x and prev_y == self.y:
            return "L"
        if prev_x == self.x and prev_y < self.y:
            return "D"
        
    
        if prev_x < self.x and prev_y > self.y:
            return "UL"
        if prev_x > self.x and prev_y > self.y:
            return "UR"
        if prev_x > self.x and prev_y < self.y:
            return "DR"
        if prev_x < self.x and prev_y < self.y:
            return "DL"
        

    def move_next(self, direction, prev_x, prev_y):
        """Move the next knot according to the current knot pos."""
        
        direction = self.determine_direction(prev_x, prev_y)

        # cardinal move
        if direction == "R":
            self.x += 1
        if direction == "U":
            self.y += 1
        if direction == "L":
            self.x -= 1
        if direction == "D":
            self.y -= 1
        if direction == "UL":
            self.x -= 1
            self.y += 1    
        if direction == "UR":
            self.x += 1
            self.y += 1
        if direction == "DL":
            self.x -= 1
            self.y -= 1
        if direction == "DR":
            self.x += 1
            self.y -= 1
        
        if self.next and self.next_is_distant():
            self.next.move_next(direction, self.x, self.y)
        
        if self.tail and not (self.x, self.y) in tail_locations:
            tail_locations.add((self.x, self.y))


class Head():

    def __init__(self, tail=False):
        self.x, self.y = 0,0
        self.next = Knot(NUM_KNOTS-1)
        self.tail = tail
        self.tail_locations = set() # for part 1
        self.tail_locations.add((0,0)) # for part 1


    def parse_command(self, command):
        direction, number = command.split(' ')[0], int(command.split(' ')[1])
        return direction, number
    

    def tail_is_distant(self):
        """Return True if tail > 1 space from head, False if not."""
        if abs(self.x - self.tail.x) > 1 or abs(self.y - self.tail.y) > 1:
            return True
        else:
            return False
    
    
    def next_is_distant(self):
        """Return True if tail > 1 space from head, False if not."""
        if abs(self.x - self.next.x) > 1 or abs(self.y - self.next.y) > 1:
            return True
        else:
            return False


    def move_head(self, direction, number):
        """Move the head and then the tail."""
        
        for i in range(number):
            if direction == 'U':
                self.y += 1
            if direction == 'R':
                self.x += 1
            if direction == 'D':
                self.y -= 1
            if direction == 'L':
                self.x -= 1
            
            if self.tail_is_distant():
                self.tail.move_tail(direction, self.x, self.y)
                if not (self.tail.x, self.tail.y) in self.tail_locations:
                    self.tail_locations.add((self.tail.x, self.tail.y))
    
    
    def move_chain(self, direction, number):
        """Move the next knot in the chain."""

        for i in range(number):
            if direction == 'U':
                self.y += 1
            if direction == 'R':
                self.x += 1
            if direction == 'D':
                self.y -= 1
            if direction == 'L':
                self.x -= 1
        
            if self.next_is_distant():
                self.next.move_next(direction, self.x, self.y)
        
    
    def print_chain(self, step):
        """Print coord repr of chain."""
        print(step)
        print(f"({self.x},{self.y})")
        next = self.next
        while next:
            print(f"({next.x},{next.y})")
            next = next.next
        
        print(
        """

        """)


def part_one():
    
    t = Tail()
    h = Head(t)
    
    for command in data:
        direction, number = h.parse_command(command)
        h.move_head(direction, number)

    return len(h.tail_locations)


def part_two():

    h = Head()

    for step, command in enumerate(data):
        direction, number = h.parse_command(command)
        h.move_chain(direction, number)
        h.print_chain(step)

    return len(tail_locations)

print(part_two())
