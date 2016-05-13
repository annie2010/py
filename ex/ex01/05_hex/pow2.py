#!/usr/bin/env python

def isPower2(num):
    i = int(num % 2)
    r = int(num / 2)
    if r==0 and i == 1:
        return True
    if r>0 and i > 0:
        return False
    else:
        return isPower2(r)
    
nums = [4, 8, 12, 50, 64, 100]
print ( [ isPower2(x) for x in nums ] )   
