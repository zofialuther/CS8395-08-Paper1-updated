```python
def procLychrel(a):
    results = [a]
    n = a
    while True:
        s = n + int(str(n)[::-1])
        if str(s) == str(s)[::-1]:
            results.append(s)
            break
        else:
            results.append(s)
            n = s
    return results

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def isLychrel(n):
    return len(procLychrel(n)) >= 501

def reverseInteger(n):
    return int(str(n)[::-1])

def seedAndRelated():
    seed = []
    related = []
    lych = []
    for x in range(1, 10001):
        s = procLychrel(x)
        sIsLychrel = len(s) >= 501
        isIn = [i for i in s[:501] if i in lych]
        isOut = [i for i in s[:501] if i not in lych]
        lych.extend(isOut)
        if sIsLychrel:
            if len(isIn) == 0:
                seed.append(x)
            else:
                related.append(x)
    totalCount = len(seed) + len(related)
    pal = [i for i in seed + related if isPalindrome(i)]
    return (totalCount, pal, seed, len(related))

if __name__ == "__main__":
    totalCount, palindromicLychrel, lychrelSeeds, relatedCount = seedAndRelated()
    print("[1..10,000] contains " + str(totalCount) + " Lychrel numbers.")
    print(str(palindromicLychrel) + " are palindromic Lychrel numbers.")
    print(str(lychrelSeeds) + " are Lychrel seeds.")
    print("There are " + str(relatedCount) + " related Lychrel numbers.")
```