day = 8
input = open(f"input{day:02d}.txt").read().splitlines()
size = len(input)

def h(pos):
    return int(input[pos[0]][pos[1]])


def visdir(pos, off):
    hei = h(pos)
    xw = pos[0]+off[0]
    yw = pos[1]+off[1]
    while 0 <= xw < size and 0 <= yw < size:
        posw = (xw, yw)
        if h(posw) >= hei:
            return False
        xw += off[0]
        yw += off[1]
    return True


def vis(pos):
    return visdir(pos, (0, 1)) or visdir(pos, (0, -1)) or visdir(pos, (1, 0)) or visdir(pos, (-1, 0))


def view(pos, off):
    hei = h(pos)
    xw = pos[0]+off[0]
    yw = pos[1]+off[1]
    result = 0
    while 0 <= xw < size and 0 <= yw < size:
        result += 1
        posw = (xw, yw)
        if h(posw) >= hei:
            return result
        xw += off[0]
        yw += off[1]
    return result


def scenic(pos):
    return view(pos, (0, 1)) * view(pos, (0, -1)) * view(pos, (1, 0)) * view(pos, (-1, 0))


parta = 0
partb = 0
for x in range(size):
    for y in range(size):
        pos = (x, y)
        if vis(pos):
            parta += 1
        partb = max(partb, scenic(pos))
print(f"Day {day}: Part A = {parta}")
print(f"Day {day}: Part B = {partb}")
