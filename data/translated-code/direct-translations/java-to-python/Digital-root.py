from typing import List
from math import log

def calcDigitalRoot(number: str, base: int) -> List[int]:
    bi = int(number, base)
    additivePersistence = 0
    if bi < 0:
        bi = abs(bi)
    biBase = base
    while bi >= biBase:
        number = ''
        while bi > 0:
            number += str(bi % base)
            bi //= base
        bi = sum(int(digit, base) for digit in number)
        additivePersistence += 1
    return [additivePersistence, bi]

if __name__ == "__main__":
    args = ["123", "456"]
    for arg in args:
        results = calcDigitalRoot(arg, 10)
        print(arg + " has additive persistence " + str(results[0]) + " and digital root of " + str(results[1]))