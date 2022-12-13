import requests
import os
from collections import Counter

USER_SESSION_ID = '53616c7465645f5fd8a9a66fd042c2cbd57b12590cd8fc39cd2e79eca0ee6f70255d1f049c85b290796ec5986b855d1f4e4591e9422c3b2ce0e62dbbb2058856'

def setup():
    if not os.path.exists("6"):
        os.mkdir("6")

        with requests.get('https://adventofcode.com/2022/day/6/input', cookies={"session": USER_SESSION_ID}) as response:
                                if response.ok:
                                    data = response.text
                                    input = open("6"+"/input.txt", "w+")
                                    input.write(data.rstrip("\n"))
                                    input.close()

    data = None
    with open("6/input.txt", 'r') as f:
        data = f.readline()
    
    return data

data = setup()


def find_start_packet_marker(data):
    """
    Two pointer approach to finding the start-of-packet marker.
    First pointer keeps track of the start position of the sequence.
    Second pointer follows and creates a count-map of chars.
    If counts are all 1, then return the first pointer.
    """

    start = 0
    end = start + 4

    while start < len(data)-4:
        seq = data[start:end]
        freqs = Counter(seq)
        if freqs.most_common()[0][1] == 1:
            return end
        start+=1
        end+=1


def find_start_message_marker(data):
    """
    Two pointer approach to finding the start-of-packet marker.
    First pointer keeps track of the start position of the sequence.
    Second pointer follows and creates a count-map of chars.
    If counts are all 1, then return the first pointer.
    """

    start = 0
    end = start + 14

    while start < len(data)-4:
        seq = data[start:end]
        freqs = Counter(seq)
        if freqs.most_common()[0][1] == 1:
            return end
        start+=1
        end+=1

start_packet = find_start_packet_marker(data)
start_message = find_start_message_marker(data)
print(start_message)
