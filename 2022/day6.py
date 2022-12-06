#!/usr/bin/env python

stream=str(open("day6.input").read().strip())


c=0
for i in range(3,len(stream)):
   c+=1
   if len(set(stream[i-3:i+1])) > 3:
      print(f'{c+3}') 
      break

c=0
for i in range(13,len(stream)):
   c+=1
   if len(set(stream[i-13:i+1])) > 13:
      print(f'{c+13}')
      break

