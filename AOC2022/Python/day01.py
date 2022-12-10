day = 1
sections = open(f"input{day:02d}.txt").read().split('\n\n')
elves = []
for section in sections:
    count = 0
    for calories in section.splitlines():
        count += int(calories)
    elves.append(count)
elves.sort(reverse=1)

parta = elves[0]
print(f"Day {day}: Part A = {parta}")
partb = sum(elves[0:3])
print(f"Day {day}: Part B = {partb}")
