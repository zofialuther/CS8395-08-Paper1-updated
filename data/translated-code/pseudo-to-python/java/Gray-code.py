```python
def grayEncode(n):
    return n ^ (n >> 1)

def grayDecode(n):
    p = n
    while (n >> 1) != 0:
        p = p ^ n
    return p

def grayEncode2(n):
    result = 0
    for exp in range(0, n > 0, n >> 1):
        nextHighestBit = (n >> 1) & 1
        if nextHighestBit == 1:
            result += ((n & 1) == 0) * (1 << exp)
        else:
            result += (n & 1) * (1 << exp)
    return result

def grayDecode2(n):
    nBits = bin(n)[2:]
    result = nBits[0]
    for i in range(1, len(nBits)):
        result += "1" if nBits[i] != result[i-1] else "0"
    return int(result, 2)

def main(args):
    print("i\tBinary\tGray\tGray2\tDecoded")
    print("=======================================")
    for i in range(32):
        print(str(i) + "\t")
        print(bin(i)[2:] + "\t")
        print(bin(grayEncode(i))[2:] + "\t")
        print(bin(grayEncode2(i))[2:] + "\t")
        print(grayDecode(grayEncode(i)))
    print("")
    
    base = pow(10, 25) + 12345678901234567890
    for i in range(5):
        test = base + i
        print("test decimal      = " + str(test))
        print("gray code decimal = " + str(grayEncode(test)))
        print("gray code binary  = " + bin(grayEncode(test))[2:])
        print("decoded decimal   = " + str(grayDecode(grayEncode(test)))
        print("decoded2 decimal  = " + str(grayDecode2(grayEncode(test)))
        print("")
```