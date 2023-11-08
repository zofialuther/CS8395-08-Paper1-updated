from typing import List
from collections import deque

def properDivs(n: int) -> List[int]:
    divs = deque()
    if n == 1:
        return list(divs)
    divs.append(1)
    for x in range(2, n):
        if n % x == 0:
            divs.append(x)

    divs = list(divs)
    divs.sort()

    return divs

if __name__ == "__main__":
    for x in range(1, 11):
        print(f"{x}: {properDivs(x)}")

    x = 0
    count = 0
    for n in range(1, 20001):
        if len(properDivs(n)) > count:
            x = n
            count = len(properDivs(n))
    print(f"{x}: {count}")