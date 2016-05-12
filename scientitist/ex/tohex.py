digits='0123456789ABCDEF'

def tohex(dec):
    x = int(dec%16)
    rest = int(dec/16)
    if (rest ==0):
        return '0x' + digits[x]
    return tohex(rest) + digits[x]


numbers = [10,0,16,32,65,100]
print ( [ tohex(n) for n in numbers ] )
