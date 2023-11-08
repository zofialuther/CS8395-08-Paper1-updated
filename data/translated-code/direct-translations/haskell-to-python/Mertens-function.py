```python
from Data.List.Split import chunksOf
import Data.MemoCombinators as Memo
from Math.NumberTheory.Primes import unPrime, factorise
from Text.Printf import printf

def moebius(n):
    factors = factorise(n)
    result = 1
    for p, e in factors:
        if unPrime(p) == 0:
            result = 0
        elif e == 1:
            result *= -1
        else:
            result = 0
    return result

def mertens(n):
    return Memo.integral(lambda n: sum(moebius(i) for i in range(1, n+1)))

def countZeros(lst):
    return len([mertens(n) for n in lst if mertens(n) == 0])

def crossesZero(lst):
    mertens_lst = [mertens(n) for n in lst]
    result = 0
    for i in range(len(mertens_lst) - 1):
        if mertens_lst[i+1] == 0 and mertens_lst[i] != 0:
            result += 1
    return result

if __name__ == "__main__":
    printf("The first 99 terms for M(1..99):\n\n   ")
    for i in range(1, 10):
        printf("%3d" % mertens(i))
    printf("\n")
    for row in chunksOf(10, list(range(10, 100))):
        for i in row:
            printf("%3d" % mertens(i))
        printf("\n")
    printf("\nM(n) is zero %d times for 1 <= n <= 1000.\n" % countZeros(list(range(1, 1001))))
    printf("M(n) crosses zero %d times for 1 <= n <= 1000.\n" % crossesZero(list(range(1, 1001))))
```