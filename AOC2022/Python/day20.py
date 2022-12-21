import os
from collections import deque
day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()
nums = [int(line) for line in lines]

def solve(part):
    tups = [(index, num * (811589153 if part == 'b' else 1)) for index, num in enumerate(nums)]
    d = deque(tups)
    size = len(d)
    for _ in range(10 if part == 'b' else 1):
        for i in range(size):
            while not d[0][0] == i:  # Find our number
                d.append(d.popleft())
            put = d.popleft()
            newpos = put[1] % (size - 1)
            d.insert(newpos, put)
    while not d[0][1] == 0:  # Find zero:
        d.append(d.popleft())
    return sum([d[1000 % size][1], d[2000 % size][1], d[3000 % size][1]])

parta = solve('a')
print(f"Day {day}: Part A = {parta}")
partb = solve('b')
print(f"Day {day}: Part B = {partb}")
