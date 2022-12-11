#!/usr/bin/env python
import numpy as np

lines = [line.strip("\n") for line in open("day11.input")]

class Monkey:
    monkeys = []
    def __init__(self, items, threat, check, winner, loser):
        self.id = len(self.monkeys)
        self.monkeys.append(self)
        self.items  = list(map(int,items))
        self.threat = threat
        self.check  = int(check)
        self.winner = int(winner)
        self.loser  = int(loser)
        self.inspections = 0

    def __getitem__(self, id):
        return self

    def worry(self):
        op,amt = self.threat.split(" ")
        if amt=='old': amt = 'self.items[0]'
        self.items[0] = eval('self.items[0]'+op+amt)

    def bored(self, relief):
        if (relief):
            self.items[0] = self.items[0]//3

    def test(self):
        rem = self.items[0] % self.check
        self.items[0] = self.items[0] % modulo
        if rem < 1:
            return self.winner
        else:
            return self.loser

    def throw(self, other):
        item, self.items = self.items[0], self.items[1:]
        other.items.append(item)

    def inspect(self):
        while(len(self.items) > 0):
            self.worry()
            self.bored(relief)
            self.throw(Monkey.monkeys[self.test()])
            self.inspections += 1

# create monkeys
def generate_monkeys(lines):
    Monkey.monkeys=[]
    for i,line in enumerate(lines):
        if (i%7 != 0): continue
        items=[int(line.strip()) for line in lines[i+1][18:].split(",")]
        ops=(' '.join(lines[i+2].split(" ")[-2:]))
        div=lines[i+3].split(" ")[-1]
        winner=lines[i+4].split(" ")[-1]
        loser=lines[i+5].split(" ")[-1]
        Monkey(items, ops, div, winner, loser)
    return

def evaluate(rounds):
    for round in range(rounds):
        for i,monkey in enumerate(Monkey.monkeys):
            monkey.inspect()

# Part 1
generate_monkeys(lines)
modulo = np.lcm.reduce([_.check for _ in Monkey.monkeys])
relief = True
evaluate(20)
print(f'Monkey business: {np.prod(sorted([_.inspections for _ in Monkey.monkeys])[-2:])}')

# Part 2
Monkey.monkeys=[]
generate_monkeys(lines)
relief = False
evaluate(10000)
print(f'Monkey business: {np.prod(sorted([_.inspections for _ in Monkey.monkeys])[-2:])}')

