#!/usr/bin/env python

digits='0123456789ABCDEF'

def tohex(num):
    i = int(num % 16)
    r = int(num / 16)
    if 0 == r:
        return '0x' + digits[i]
    else:
        return tohex(r) + digits[i] 

nums = [20,30,32, 100]
print ([tohex(x) for x in nums])

