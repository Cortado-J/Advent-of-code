import os
day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()
print(lines)

parta = 7777
partb = 7777
print(f"Day {day}: Part A = {parta}")
print(f"Day {day}: Part B = {partb}")
