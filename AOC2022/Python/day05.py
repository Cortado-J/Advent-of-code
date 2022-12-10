day = 5
sections = open(f"input{day:02d}.txt").read().split('\n\n')
inputstacks = sections[0].splitlines()
moves = sections[1].splitlines()

import copy

stacks = [list() for _ in range(0, 9)]
for row in range(7, -1, -1):
    for stack in range(0, 9):
        ch = inputstacks[row][stack * 4 + 1]
        if ch != ' ':
            stacks[stack].append(ch)
keepstacks = copy.deepcopy(stacks)

def move(fr, to):
    stacks[to - 1].append(stacks[fr - 1].pop())

def multimove(fr, to, n):
    for _ in range(0, n):
        move(fr, to)

for line in moves:
    bits = line.split(' ')
    m = int(bits[1])
    f = int(bits[3])
    t = int(bits[5])
    multimove(f, t, m)

parta = ''.join([s[-1] for s in stacks])

stacks = copy.deepcopy(keepstacks)
stacks.append(list())  # stack 10
for line in moves:
    bits = line.split(' ')
    m = int(bits[1])
    f = int(bits[3])
    t = int(bits[5])
    multimove(f, 10, m)
    multimove(10, t, m)

partb = ''.join([s[-1] for s in stacks[0:9]])

print(f"Day {day}: Part A = {parta}")
print(f"Day {day}: Part B = {partb}")
