import os

day = int(os.path.basename(__file__)[-5:-3])
filename = f"input{day:02d}.txt"
lines = open(filename).read().splitlines()
jobs = dict()
memo = dict()
for line in lines:
    bits = line.split(':')
    jobs[bits[0]] = bits[1][1:]


# For Part A, yell should be set to None and then the existing value for Humn will be used
def evaluate(m, yell):
    global jobs
    if m == 'humn':
        if yell is not None:
            return yell
    if m in memo:
        return memo[m]
    result = None
    if m.isnumeric():
        result = int(m)
    elif m in jobs:
        result = evaluate(jobs[m], yell)
    else:
        bits = m.split(' ')
        if len(bits) == 1:
            result = evaluate(m, yell)
        else:
            left = evaluate(bits[0], yell)
            right = evaluate(bits[2], yell)
            if bits[1] == '+':
                result = left + right
            elif bits[1] == '-':
                result = left - right
            elif bits[1] == '*':
                result = left * right
            elif bits[1] == '/':
                result = left / right
    memo[m] = result
    return result


parta = int(evaluate('root', None))
print(f"Day {day}: Part A = {parta}")

jobs['root'] = jobs['root'].replace('+', '-')


def compare(yell):
    global memo
    memo = {}
    return evaluate('root', yell)


def findbinary(lo, hi):
    while hi > lo:
        mid = (hi + lo) // 2
        switch = compare(hi) > compare(lo)
        midcomp = compare(mid)
        # print(f"low={lo}, hi={hi}, mid={mid}, compare(mid)={midcomp}")
        if midcomp == 0:
            return mid
        if (midcomp > 0) ^ switch:
            lo = mid
        else:
            hi = mid


partb = findbinary(0, 10 ** 20)
print(f"Day {day}: Part B = {partb}")
