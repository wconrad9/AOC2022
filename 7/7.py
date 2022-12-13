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

    data = []
    with open(f"{day}/input.txt", 'r') as f:
        line = f.readline()
        while line:
            data.append(line.removesuffix('\n'))
            line = f.readline()
    
    return data

data = setup('7')


def parse_line(line:str):

    current_dir = dirstack[len(dirstack) - 1] if len(dirstack) else None

    # command cd or ls
    if line.startswith('$'):
        command = line.split(' ')[1]

        if command == 'cd':
            dest = line.split(' ')[2]
            if dest == '..':
                dir = dirstack.pop()
                dir_hist[dir.location] = dir.size
                return
            else:
                dirstack.append(Dir(current_dir.location + '/' + dest, current_dir))
                return
        else: # command is ls
            return
    
    # ls contents
    else:
        if line.split(' ')[0] == 'dir':
            return
        else:
            size = line.split(' ')[0]
            current_dir.increment_size(size)
            return

# idea:
# for every dir encountered, create a dir object
# when ls is called, add sizes to the dir object
# recurse until a point when there are no more dir objects
# if a dir object is encountered during ls, add to the stack


class Dir():

    size = 0

    def __init__(self, location, parent_dir):
        self.location = location
        self.parent_dir = parent_dir
    
    def increment_size(self, amount):
        
        if self.parent_dir:
            self.parent_dir.increment_size(amount)

        self.size += int(amount)
        

    def __str__(self):
        return(f"{self.location}, {self.size}")

dirstack: Dir = []
dir_hist = {}

dirstack.append(Dir('/', None))

for line in data[1:]:
    parse_line(line)

# part 1
total = 0
for k, v in dir_hist.items():
    if v <= 100000:
        total+=v

print(total)

# 70000000 - '/'.size = 19783544
# 30000000 - 19783544 = 10216456
# we need to free at least 10216456 bytes. What is the smallest directory we can delete to do so?
# part 2

min_greater = sys.maxsize
cutoff = 10216456
for k, v in dir_hist.items():
    if v >= cutoff and v < min_greater:
        min_greater = v

print(min_greater)

