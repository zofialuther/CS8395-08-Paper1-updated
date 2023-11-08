```python
import time
import math

def prime(N):
    if (N % 2 == 0):
        return False
    M = math.floor(math.sqrt(N)) - 1
    Max = math.floor(M / 2)
    for I in range(1, Max + 1):
        if (N % (2 * I + 1) == 0):
            return False
    return True

def primesByDiffs(Primes, Diff):
    if (len(Diff) == 0):
        return []
    Slides = []
    Len0 = len(Diff)
    Len = Len0 + 1
    for i in range(len(Primes)):
        Slide = []
        for j in range(Len):
            Slide.append(Primes[i + j])
        Slides.append(Slide)
    return Slides

def select(Diffs, Slide):
    if (len(Diffs) == 0):
        return Slide
    S1 = Slide[0]
    S2 = S1 + Diffs[0]
    Stail = Slide[1:]
    return select(Diffs[1:], [S2] + Stail)

def run(Diffs, PrimeList):
    if (len(Diffs) == 0):
        return
    Start = time.time()
    SlideList = primesByDiffs(PrimeList, Diffs[0])
    Num = len(SlideList)
    Stop = time.time()
    Runtime = Stop - Start
    First = SlideList[0]
    print(f'number: {Num} [time(ms): {Runtime}] first: {First}')
    if (len(SlideList) > 1):
        Last = SlideList[-1]
        print(f'last: {Last}')
    run(Diffs[1:], PrimeList)

def do():
    Num = 1000000
    Start = time.time()
    List = [i for i in range(2, Num + 1)]
    PrimeList = list(filter(prime, List))
    NumPrimes = len(PrimeList)
    Stop = time.time()
    RunTime = Stop - Start
    print(f'there are {NumPrimes} primes until {Num} [time(ms): {RunTime}]')
    DiffList = [[1], [2], [2, 2], [2, 4], [4, 2], [2, 4, 6], [2, 6, 4], [4, 2, 6], [4, 6, 2], [6, 2, 4], [6, 4, 2]]
    run(DiffList, PrimeList)
```