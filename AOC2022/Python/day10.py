day = 10
lines = open(f"input{day:02d}.txt").read().splitlines()

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
print(f"Day {day}: Part A = {parta}")

display = ["#" if abs(sig[pix]-pix % 40) <= 1 else ' ' for pix in range(40*6)]

prep = ''.join(display)
for row in range(6):
    print(prep[row*40:(row+1)*40])

partb='EZFCHJAB' # Manually typed in
print(f"Day {day}: Part B = {partb}")
