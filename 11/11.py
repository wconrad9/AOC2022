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

data = setup('11')