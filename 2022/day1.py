#!/usr/bin/env python

A=B=[]
f = open("day1.input", "r")
for x in f:
   if x != '\n':
      A+=int(x),
   else:
      B,A=B+[sum(A)],[]

print('Part 1:',max(B))
print('Part 2:',sum(sorted(B)[-3:]))
