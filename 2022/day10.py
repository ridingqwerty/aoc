#!/usr/bin/env python
import numpy as np

lines = [l.strip() for l in open("day10.input")]
buffer=np.zeros((6,40), dtype=str)

cycle=0
X=1
sigs=[]
breakpoints=[40*x+60 for x in range(6)]

def SS():
    global breakpoints
    if (cycle in breakpoints):
        breakpoints=breakpoints[1:]
        sigs.append(X*cycle)

def draw():
    buffer[cycle//40][cycle%40] = ['.','#'][abs(cycle%40 - (X)) < 2]

def noop():
    global cycle
    draw()
    cycle=cycle+1
    SS()

def addx(n):
    global X
    noop()
    X = X + n 
    SS()

for line in lines:
    if(line.split()[0] == 'noop'):
        noop()
    else:
        noop()
        addx(int(line.split()[1]))
        SS()

print(f'total={sum(sigs)}')
[print(''.join(buffer[i])) for i in range(len(buffer))]

