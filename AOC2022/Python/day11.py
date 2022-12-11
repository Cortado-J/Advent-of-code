import numpy as np
np.seterr(all='raise')

day = 11
inp = open(f"input{day:02d}.txt").read().split('\n\n')
monkeys = len(inp)

class Part:
    divby3 = True

    def __init__(self, divby3):
        self.divby3 = divby3

        self.items = []
        self.ops = []
        self.factors = []
        self.divs = []
        self.acttrue = []
        self.actfals = []
        self.inspect = []
        for monkey in inp:
            # Monkey 0:
            lines = monkey.splitlines()
            # Starting items: 57, 58
            gath = []
            for x in lines[1].split(' ')[4:]:
                if x[-1] == ',':
                    x = x[0:-1]
                gath.append(int(x))
            self.items.append(gath)
            # Operation: new = old * 19
            op = lines[2].split(' ')[-2]
            # Test: divisible by 7
            fact = lines[2].split(' ')[-1]
            if fact == 'old':
                fact = '2'
                op = 'pow'
            fact = int(fact)
            self.ops.append(op)
            self.factors.append(fact)
            self.divs.append(int(lines[3].split(' ')[-1]))
            #   If true: throw to monkey 2
            self.acttrue.append(int(lines[4].split(' ')[-1]))
            #   If false: throw to monkey 3
            self.actfals.append(int(lines[5].split(' ')[-1]))

        self.modulus = np.prod(self.divs)

    def operate(self, x, op, fact):
        if op == '+':
            return x + fact
        if op == '*':
            return x * fact
        if op == 'pow':
            return x * x
        return -7777777


    def domonk(self, m):
        for worry in self.items[m]:
            self.inspect[m] += 1
            worry = self.operate(worry, self.ops[m], self.factors[m]) % self.modulus
            if self.divby3:
                worry = worry // 3
            dest = self.acttrue[m] if worry % self.divs[m] == 0 else self.actfals[m]
            # print(f"Monkey {m} throws item with worry {worry} to monkey {dest}")
            self.items[dest].append(worry)
        self.items[m] = []


    def round(self):
        for monk in range(monkeys):
            self.domonk(monk)
        # print(self.items)

    def run(self, rounds):
        self.inspect = [0 for _ in range(monkeys)]
        for r in range(rounds):
            self.round()
        biggest = sorted(self.inspect, reverse=True)
        return biggest[0] * biggest[1]


pa = Part(True)
parta = pa.run(20)
print(f"Day {day}: Part A = {parta}")

pb = Part(False)
partb = pb.run(10000)
print(f"Day {day}: Part B = {partb}")
