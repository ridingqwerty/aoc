#!/usr/bin/env python

import numpy as np

lines=[l.strip() for l in open("day9.input").readlines()]

def update_head(head, dir):
    if dir=='U': return (head[0], head[1]+1)
    if dir=='D': return (head[0], head[1]-1)
    if dir=='L': return (head[0]-1, head[1])
    if dir=='R': return (head[0]+1, head[1])

def update_tail(tail, head):
    while abs(head[0] - tail[0]) > 1 or abs(d2:=head[1] - tail[1]) > 1:
       tail = (tail[0]+np.sign(head[0] - tail[0]),tail[1]+np.sign(head[1] - tail[1]))
    return tail

def update_board(board, tail):
    board[(tail)] = True
    return board

def simulate_rope(knots=2):
    dim = (1000, 1000)
    start = (0,0)
    rope = [start for _ in range(knots)]
    board = np.zeros(dim, dtype=bool)
    board[(rope[-1])] = True
    
    for line in lines:
        d, s = line.split()
        s = int(s)
        while s > 0:
            rope[0] = update_head(rope[0], d) 
            for i in range(len(rope[1:])):
                rope[i+1] = update_tail(rope[i+1], rope[i])
            board = update_board(board, rope[-1])
            s = s - 1
    return sum(sum(board))

print(f'Part 1: {simulate_rope(2)}')
print(f'Part 2: {simulate_rope(10)}')

# part 1 answer: 6057 (sample: 13)
# part 2 answer: 2514 (p1 sample: 1, p2 sample: 36)
