#!/usr/bin/env python
import numpy as np

A=np.array([list(map(int,line.strip())) for line in open("day8.input")])
B=A.T

def pmax(n):
    try: return max(n)
    except: return 0

def look(n, a):
    score=0
    for x in a:
        score += 1
        if x >= n: break
    return score

visible_trees = 0
scenic = []

for i in range(len(A)**2):
    row,col=i//len(A),i%len(A)
    n = A[row][col]
    east=A[row][:col][::-1]
    west=A[row][col+1:]
    north=B[col][:row][::-1]
    south=B[col][row+1:]

    # part 1
    if not (pmax(east)>=n<=pmax(west) and pmax(north)>=n<=pmax(south) and (row%(len(A)-1))*(col%(len(A)-1))) != 0:
       visible_trees+=1 

    # part 2
    u,d,l,r=0,0,0,0
    u=look(n,east)
    d=look(n,west)
    l=look(n,north)
    r=look(n,south)
 
    scenic += u*d*l*r,

print(f'{visible_trees} trees visible')
print(f'{max(scenic)} max scenic score')
