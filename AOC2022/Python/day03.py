day = 3
lines = open(f"input{day:02d}.txt").read().splitlines()

def priority(ch):
    if ord(ch) > 96:
        return ord(ch)-96
    else:
        return ord(ch)-64+26

def common(x,y):
    gather = ''
    for ch1 in x:
        for ch2 in y:
            if ch1 == ch2:
                gather += ch1
    return gather

def value(sack):
    return priority(common(sack[0:len(sack)//2], sack[len(sack)//2:len(sack)])[0])

parta = sum([value(line) for line in lines])
print(f"Day {day}: Part A = {parta}")

partb = 0
for base in range(0, len(lines), 3):
    firsttwo = common(lines[base], lines[base+1])
    all = common(firsttwo, lines[base + 2])
    partb += priority(all[0])

print(f"Day {day}: Part B = {partb}")
