def sum35(n):
    f = sumMul(n)
    return f(3) + f(5) - f(15)

def sumMul(n, f):
    n1 = (n - 1) / f
    return f * n1 * (n1 + 1) / 2

def main():
    values = [sum35(1000), sum35(100000000000000000000000000000000), sumMulS(1000, [3, 5]), sumMulS(10000000, [2, 3, 5, 7, 11, 13])]
    mapM_(print, values)

def pairLCM(arr):
    if not arr:
        return []
    else:
        x = arr[0]
        xs = arr[1:]
        return lcm(x, xs) + pairLCM(xs)

def sumMulS(n, s):
    uniqueS = removeDuplicates(s)
    f = sumMul(n)
    g = sumMulS(n)
    return sum(f) - sum(g(uniqueS))

def removeDuplicates(arr):
    return list(set(arr))