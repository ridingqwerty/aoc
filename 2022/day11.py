#!/usr/bin/env python
import numpy as np

lines = [line.strip("\n") for line in open("day11.sample")]
#relief = True

class Monkey:
    monkeys = []
    modulo=0
    def __init__(self, items, threat, check, winner, loser):
        self.id = len(self.monkeys)
        self.monkeys.append(self)
        self.items  = list(map(int,items))
        self.threat = threat
        self.check  = int(check)
        self.winner = int(winner)
        self.loser  = int(loser)
        self.inspections = 0
        self.update_modulo(self.get_modulo())

    def __getitem__(self, id):
        return self

    @classmethod
    def update_modulo(self, new_modulo):
        self.modulo = new_modulo
        return self.modulo

    @classmethod
    def get_modulo(self):
        modulo = np.prod([_.check for _ in Monkey.monkeys])
        return modulo

    def worry(self):
        op,amt = self.threat.split(" ")
        if amt=='old': amt = 'self.items[0]'
        self.items[0] = eval('self.items[0]'+op+amt)

    def bored(self, relief):
        if (relief): self.items[0] = self.items[0]//3

    def test(self):
        rem = self.items[0] % self.check
        self.items[0] = self.items[0] % Monkey.modulo
        if rem < 1: return self.winner
        else: return self.loser

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
        div,winner,loser=[x.split(" ")[-1] for x in lines[i+3:i+6]]
        Monkey(items, ops, div, winner, loser)
    return

def evaluate(rounds):
    for round in range(rounds):
        for i,monkey in enumerate(Monkey.monkeys):
            monkey.inspect()

def Main():
    global relief
    for rounds,relieved in zip((20,10000),(True,False)):
        relief = relieved
        generate_monkeys(lines)
        evaluate(rounds)
        print(f'Monkey business: {np.prod(sorted([_.inspections for _ in Monkey.monkeys])[-2:])}')
    return

Main()
#Monkey business: 10605
#Monkey business: 2713310158

