lines = """addx 2
addx 3
addx 1
noop
addx 4
addx 1
noop
addx 28
addx -24
noop
addx 5
addx 17
addx -16
noop
addx 6
noop
addx -7
addx 11
addx 4
noop
addx 1
addx -36
addx -2
noop
noop
addx 10
noop
noop
addx -2
addx 2
addx 25
addx -18
addx 23
addx -22
addx 2
addx 5
addx -10
addx -15
addx 28
addx 2
addx 5
addx 2
addx -16
addx 17
addx -36
noop
noop
addx 39
addx -32
addx -5
addx 7
addx 1
addx 5
addx -13
addx 1
addx 17
addx 1
noop
addx 7
noop
addx -2
addx 2
addx 5
addx 2
noop
noop
noop
noop
addx -37
noop
noop
noop
noop
addx 6
addx 11
addx -7
addx 29
addx -22
addx 5
noop
noop
noop
addx 3
noop
addx 7
addx -28
addx 24
addx 3
addx 2
noop
addx 2
noop
addx 3
addx -38
noop
addx 7
addx -2
addx 1
addx 6
addx -10
addx 38
addx -25
addx 5
addx 2
addx -10
addx 11
addx 2
noop
addx 3
addx 2
noop
addx 3
addx 2
addx 5
addx -39
addx 1
addx 1
addx 3
addx 2
addx 4
addx 29
addx -23
noop
addx -1
addx 5
noop
addx 11
addx -10
addx 5
addx -1
noop
addx 3
noop
addx 3
addx 4
noop
noop
noop
noop
noop""".splitlines()

# lines = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop""".splitlines()


x=1
sig = []

def step():
    sig.append(x)

step()

for line in lines:
    bits = line.split(' ')
    cmd = bits[0]
    if cmd == 'addx':
        step()
        x += int(bits[1])
        step()
    elif cmd == 'noop':
        step()

def ss(cyc):
    return cyc * sig[cyc-1]

parta=ss(20)+ss(60)+ss(100)+ss(140)+ss(180)+ss(220)
print("Part A = ", parta)

display = ["#" if abs(sig[pix]-pix % 40) <= 1 else '.' for pix in range(40*6)]

prep = ''.join(display)
for row in range(6):
    print(prep[row*40:(row+1)*40])

partb='EZFCHJAB' # Manually typed in
print("Part B = ", partb)
