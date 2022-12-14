import os
import copy
day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()

grid = {}
height = len(lines)
width = len(lines[0])
start = (0,0)
end = (0,0)
for row in range(height):
    for col in range(width):
        ch = lines[row][col]
        pos = (row, col)
        if ch == 'S':
            start = pos
            ch = 'a'
        elif ch == 'E':
            end = pos
            ch = 'z'
        grid[pos] = ord(ch) - ord('a')

def shortest(startpos):
    dirs = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'V'), (-1, 0, '^')]
    distances = {}
    def expand(pos, distance):
        for dir in dirs:
            newpos = (pos[0] + dir[0], pos[1] + dir[1])
            if newpos not in distances and newpos in grid and grid[newpos] <= grid[pos]+1:
                distances[newpos] = distance

    def allexpand(distance):
        for pos in grid:
            if pos in distances:
                if distances[pos] == distance:
                    expand(pos, distance+1)

    distance = 1
    expand(startpos, distance)
    while end not in distances:
        allexpand(distance)
        distance += 1
    return distances[end]


parta = shortest(start)
print(f"Day {day}: Part A = {parta}")

startcol = 0
shortestshortest = 1000000
for startrow in range(height):
    startpos = (startrow, startcol)
    shortestshortest = min(shortestshortest, shortest(startpos))

partb = shortestshortest
print(f"Day {day}: Part B = {partb}")

