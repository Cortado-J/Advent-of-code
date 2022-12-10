day = 6
input = open('input' + str(day) + '.txt').read()
# input="bvwbjplbgvbhsrlpgdmjqwftvncz"

def start(length):
    for i in range(length - 1, len(input)):
        s = input[i - length + 1:i + 1]
        if len(set(s)) == length:
            return (i + 1)

print(start(4))
print(start(14))
