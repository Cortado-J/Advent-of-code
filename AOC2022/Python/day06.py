day = 6
input = open(f"input{day:02d}.txt").read()
# input="bvwbjplbgvbhsrlpgdmjqwftvncz"

def start(length):
    for i in range(length - 1, len(input)):
        s = input[i - length + 1:i + 1]
        if len(set(s)) == length:
            return (i + 1)

parta = start(4)
partb = start(14)
print(f"Day {day}: Part A = {parta}")
print(f"Day {day}: Part B = {partb}")
