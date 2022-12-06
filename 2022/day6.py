#!/usr/bin/env python

stream=str(open("day6.input").read().strip())

def decode(stream, tkn_len):
   c=0
   tkn_len-=1
   for i in range(tkn_len,len(stream)):
      c+=1
      if len(set(stream[i-tkn_len:i+1])) > tkn_len:
          return c+tkn_len

print(f'{decode(stream,4)}')
print(f'{decode(stream,14)}')

