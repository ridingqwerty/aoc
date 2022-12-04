#!/usr/bin/env python

R=S=0
for L in [l.strip() for l in open("day4.input")]:
   a,b=L.split(',')
   x,y=list(map(int,a.split('-')))
   u,v=list(map(int,b.split('-')))
   r=sorted(list(set(range(x,y+1)) & set(range(u,v+1))))
   if r != []:
     R+=1
     if (x,y)==(r[0],r[-1]) or (u,v)==(r[0],r[-1]): S+=1
print(S)
print(R)

