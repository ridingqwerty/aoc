#!/usr/bin/env python

D=E=0
for x in open("day2.input"):
 a=ord(x[0])-ord('A')
 b=ord(x[2])-ord('X')
 E+=[((a-1)%3)+1,a+4,((a+1)%3)+7][b]
 if a==b: D+=b+4;continue
 D+=[b+7,b+1][(a-1)%3==b]

print("Day 2, part 1:", D)
print("Day 2, part 2:", E)
