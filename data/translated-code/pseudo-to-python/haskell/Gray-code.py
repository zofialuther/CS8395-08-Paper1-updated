def grayToBin(g):
    if g == 0:
        return 0
    else:
        return g ^ grayToBin(g >> 1)

def binToGray(b):
    return b ^ (b >> 1)

def showBinary(n):
    return format(n, 'b')

def showGrayCode(num):
    bin_num = showBinary(num)
    gray_num = showBinary(binToGray(num))
    print("int: %2d -> bin: %5s -> gray: %5s" % (num, bin_num, gray_num))

def main():
    for num in range(32):
        showGrayCode(num)

main()