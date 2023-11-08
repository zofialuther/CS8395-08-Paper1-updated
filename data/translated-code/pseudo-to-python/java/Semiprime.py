from typing import List
from math import isqrt
from sympy import isprime

def primeDecomp(a: int) -> List[int]:
    if a < 2:
        return None
    result = []
    while a % 2 == 0:
        a //= 2
        result.append(2)
    if a != 1:
        b = 3
        while b <= isqrt(a):
            if isprime(b):
                if a % b == 0:
                    result.append(b)
                    a //= b
            b += 2
        result.append(a)
    return result

def isSemi(x: int) -> bool:
    decomp = primeDecomp(x)
    return decomp is not None and len(decomp) == 2

def main():
    for i in range(2, 101):
        if isSemi(i):
            print(i, end=" ")
    print("\n")
    for i in range(1675, 1681):
        if isSemi(i):
            print(i, end=" ")

main()