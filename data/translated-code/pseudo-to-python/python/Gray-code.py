def int2bin(n):
    if n != 0:
        bits = []
        while n != 0:
            n, remainder = divmod(n, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

def bin2int(bits):
    i = 0
    for bit in bits:
        i = i * 2 + bit
    return i