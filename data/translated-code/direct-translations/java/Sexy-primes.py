```python
MAX = 1_000_035
primes = [True] * MAX

def sieve():
    for i in range(2, MAX):
        primes[i] = True
    for i in range(2, MAX):
        if primes[i]:
            for j in range(2*i, MAX, i):
                primes[j] = False

def main():
    sieve()
    pairs = 0
    pairList = []
    triples = 0
    tripleList = []
    quadruplets = 0
    quadrupletList = []
    unsexyCount = 1
    unsexyList = []
    for i in range(3, MAX):
        if i-6 >= 3 and primes[i-6] and primes[i]:
            pairs += 1
            pairList.append(str(i-6) + " " + str(i))
            if len(pairList) > 5:
                pairList.pop(0)
        elif i < MAX-2 and primes[i] and not (i+6<MAX and primes[i] and primes[i+6]):
            unsexyCount += 1
            unsexyList.append(str(i))
            if len(unsexyList) > 10:
                unsexyList.pop(0)
        if i-12 >= 3 and primes[i-12] and primes[i-6] and primes[i]:
            triples += 1
            tripleList.append(str(i-12) + " " + str(i-6) + " " + str(i))
            if len(tripleList) > 5:
                tripleList.pop(0)
        if i-16 >= 3 and primes[i-18] and primes[i-12] and primes[i-6] and primes[i]:
            quadruplets += 1
            quadrupletList.append(str(i-18) + " " + str(i-12) + " " + str(i-6) + " " + str(i))
            if len(quadrupletList) > 5:
                quadrupletList.pop(0)
    print(f"Count of sexy triples less than {MAX:,d} = {pairs}")
    print(f"The last 5 sexy pairs:\n  {', '.join(pairList)}\n")
    print(f"Count of sexy triples less than {MAX:,d} = {triples}")
    print(f"The last 5 sexy triples:\n  {', '.join(tripleList)}\n")
    print(f"Count of sexy quadruplets less than {MAX:,d} = {quadruplets}")
    print(f"The last 5 sexy quadruplets:\n  {', '.join(quadrupletList)}\n")
    print(f"Count of unsexy primes less than {MAX:,d} = {unsexyCount}")
    print(f"The last 10 unsexy primes:\n  {', '.join(unsexyList)}\n")

if __name__ == "__main__":
    main()
```