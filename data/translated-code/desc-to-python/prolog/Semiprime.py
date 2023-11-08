```python
def factors(N, FList):
    for i in range(1, N+1):
        if N % i == 0:
            FList.append(i)

def semiPrimeList(limit):
    semiPrimes = []
    for i in range(2, limit+1):
        FList = []
        factors(i, FList)
        if len(FList) == 2:
            semiPrimes.append(i)
    return semiPrimes

def do(start, end):
    result = semiPrimeList(end)
    for num in result:
        if num >= start:
            print(num)

do(10, 100)
```