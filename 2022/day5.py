#!/usr/bin/env python
import numpy as np
import copy

A=I=[]
H="day5.input"


# turn input to a list of strings
L=[l for l in open(H)]
I=[l for l in L[L.index('\n')+1:]]
A = [list(''.join(l).strip()) for l in [ ''.join(x) for x in [ x[1:] for x in [ x[::-1] for x in np.array([[x for x in l if x!='\n']for l in [l for l in L[:L.index('\n')]]]).T.tolist() if '1' <= x[-1] <= '9' ]]]]
B = copy.deepcopy(A)

for i in I:
   x,y,z=map(int,[i.strip() for i in i.split(" ")][1::2])

   y-=1
   z-=1
   A[z]+=A[y][-x:];[A[y].pop() for _ in A[y][-x:]]
   [B[z].append(B[y].pop()) for _ in range(x)]

print("part 1 answer:")
print(''.join([b[-1] for b in B]))

print("part 2 answer:")
print(''.join([a[-1] for a in A]))
