from itertools import permutations
from functools import reduce
from math import gcd

def main():
    digits = [1, 2, 3, 4, 6, 7, 8, 9]
    lcmDigits = reduce(lcm, digits)
    sevenDigits = [delete(digits, x) for x in [1, 4, 7]]

    maxNum = 0
    for perm in concatMap(permutations, sevenDigits):
        num = intFromDigits(perm)
        if num % lcmDigits == 0 and num > maxNum:
            maxNum = num

    print(maxNum)

def intFromDigits(xs):
    return reduce(lambda a, x: a * 10 + x, xs, 0)

def concatMap(f, xs):
    result = []
    for item in xs:
        mapped = f(item)
        result.extend(mapped)
    return result

def delete(xs, x):
    ys = xs.copy()
    ys.remove(x)
    return ys

def lcm(x, y):
    return 0 if (x == 0 or y == 0) else abs(y * (x // gcd(x, y)))

main()