#!/usr/bin/env python

L=[line.strip() for line in open("day3.input")]
Z=list(map(chr,[*range(97,123),*range(65,91)]))
Q=lambda n:ord(n)-[38,96]['a'<=y<='z']

R=S=0
for i in range(len(L)//3):
 for y in Z:
  a,b,c=L[3*i:3*i+3]
  if all(y in d for d in [a,b,c]):
   S+=Q(y)
  for d in [a,b,c]: 
   if y in d[:len(d)//2] and y in d[len(d)//2:]:
    R+=Q(y)
print(f'Day 3, part 1: {R}')
print(f'Day 3, part 2: {S}')

#~/code/python/aoc/2022 ▶ ./day3.py
#Day 3, part 1: 8252
#Day 3, part 2: 2828

