import os

day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()


def getdigit(n, pos):
    startfactor = sum([5 ** i for i in range(pos + 1)])
    return "=-012"[((n + 2 * startfactor) // (5 ** pos)) % 5]


def snafu(n):
    result = ''
    for pos in range(40):  # Max 40 digits
        result = getdigit(n, pos) + result
    while len(result) > 0 and result[0] == '0':
        result = result[1:]  # Strip leading zeroes
    return result


def dec(s):
    acc = 0
    for d in s:
        acc = acc * 5 + '=-012'.index(d) - 2
    return acc


parta = snafu(sum([dec(s) for s in lines]))
print(f"Day {day}: Part A = {parta}")
