#!/usr/bin/env python
import numpy as np

lines=[line.strip() for line in open("day13.input")]

# Part 1
def check(left, right):
    for l, r in zip(left, right):
        if type(l) == type(r):
            if type(l) == int and l != r: return l < r
            if type(l) == list and check(l,r) != None: return check(l,r)
        elif type(l) != type(r):    
            if type(l) == int and check([l],r) != None: return check([l],r) 
            if type(l) == list and  check(l,[r]) != None: return check(l,[r])

    if len(left) != len(right): return len(left) < len(right)
    return None

index_sum = 0
for i in range(0, len(lines), 3):
    left, right = map(eval, [lines[i], lines[i+1]])
    if check(left,right) == True:
        index_sum += i//3 + 1

print(f'Part 1: {index_sum}')

# Part 2
def bubsort(packets):
    for i in range(len(packets)-1):
        for j in range(len(packets)-i-1):
            if check(packets[j+1],packets[j]):
                packets[j], packets[j+1] = packets[j+1], packets[j]
    return packets

def find_packet(packets, packet):
    target = packet
    for i in range(len(packets)):
        if packets[i] == target:
            return i+1
    
packets = [eval(p) for p in lines if p != '']
divider_packets = [[[2]],[[6]]]
packets = bubsort(packets + divider_packets)
print(f'Part 2: {np.prod([find_packet(packets, x) for x in divider_packets])}')

