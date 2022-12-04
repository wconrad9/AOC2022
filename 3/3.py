import requests
import os

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

def setup():
    if not os.path.exists("2"):
                os.mkdir("2")

    with requests.get('https://adventofcode.com/2022/day/3/input', cookies={"session": USER_SESSION_ID}) as response:
                            if response.ok:
                                data = response.text
                                input = open("3"+"/input.txt", "w+")
                                input.write(data.rstrip("\n"))
                                input.close()

def partOne():
    # need to find the common character between the two strings
    points = 0
    with open('3/input.txt', 'r') as data:
        line = data.readline()

        while line:
            first_half = line[:1+len(line)//2]
            second_half = line[len(line)//2:]

            for char in first_half:
                if char in second_half:
                    if char.islower():
                        points += (ord(char) - 96)
                        break
                    else:
                        points += (ord(char) - 38)
                        break
                    
            line = data.readline()

    return points

def partTwo():
    # separate the lines into groups of three, search for a common character between all three
    
    points = 0
    with open('3/input.txt') as data:
        
        first_elf = data.readline()

        while first_elf:
            second_elf = data.readline()
            third_elf = data.readline()

            for item in first_elf:
                if item in second_elf:
                    if item in third_elf:
                        if item.islower():
                            points += ord(item) - 96
                            break
                        else:
                            points += ord(item) - 38
                            break

            first_elf = data.readline()
        
        return points

print(partTwo())