import requests
import os
import math

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

def setup():
    if not os.path.exists("4"):
                os.mkdir("4")

    # with requests.get('https://adventofcode.com/2022/day/4/input', cookies={"session": USER_SESSION_ID}) as response:
    #                         if response.ok:
    #                             data = response.text
    #                             input = open("4"+"/input.txt", "w+")
    #                             input.write(data.rstrip("\n"))
    #                             input.close()

    data = []
    with open('4/input.txt', 'r') as f:
        line = f.readline()

        while line:
            data.append(line.removesuffix("\n"))
            line = f.readline()
    
    return data

data = setup()


def part_one():

    count = 0
    for row in data:
        first, second = row.split(',')
        first_min, first_max = int(first.split('-')[0]), int(first.split('-')[1])
        second_min, second_max = int(second.split('-')[0]), int(second.split('-')[1])

        if first_min <= second_min and first_max >= second_max:
            count+=1
            continue
        
        if second_min <= first_min and second_max >= first_max:
            count+=1
            continue
    
    return count


def part_two():

    count = 0
    for row in data:
        first, second = row.split(',')
        first_min, first_max = int(first.split('-')[0]), int(first.split('-')[1])
        second_min, second_max = int(second.split('-')[0]), int(second.split('-')[1])

        if first_min >= second_min and first_min <= second_max:
            count+=1
            continue

        if first_max >= second_min and first_max <= second_max:
            count+=1
            continue
        
        if second_min >= first_min and second_min <= first_max:
            count+=1
            continue

        if second_max >= first_min and second_max <= first_max:
            count+=1
            continue
    
    return count

print(part_two())