def isEven(num):
    if num.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO):
        return True
    else:
        return False