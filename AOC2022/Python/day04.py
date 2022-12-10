day = 4
lines = open(f"input{day:02d}.txt").read().splitlines()

ta = 0
tb = 0
for line in lines:
    elves = line.split(',')
    a = elves[0].split('-')
    b = elves[1].split('-')
    ab = int(a[0])
    ae = int(a[1])
    bb = int(b[0])
    be = int(b[1])
    if ((ab >= bb and ae <= be) or (bb >= ab and be <= ae)):
        ta += 1
    if max(ab, bb) <= min(ae, be):
        tb += 1

print(f"Day {day}: Part A = {ta}")
print(f"Day {day}: Part B = {tb}")
