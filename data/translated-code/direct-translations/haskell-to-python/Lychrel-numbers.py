```python
def procLychrel(a):
    def pl(n):
        s = n + int(str(n)[::-1])
        if isPalindrome(s):
            return [s]
        else:
            return [s] + pl(s)
    return [a] + pl(a)

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def isLychrel(n):
    return len(procLychrel(n)) > 500

def reverseInteger(n):
    return int(str(n)[::-1])

def seedAndRelated():
    seed = []
    related = []
    lych = []
    for x in range(1, 10001):
        s = procLychrel(x)
        sIsLychrel = len(s) > 500
        isIn, isOut = [], []
        for num in s[:501]:
            if num in lych:
                isIn.append(num)
            else:
                isOut.append(num)
        newLych = lych + isOut
        if sIsLychrel:
            if not isIn:
                seed.append(x)
                lych = newLych
            else:
                related.append(x)
                lych = newLych
    totalCount = len(seed) + len(related)
    pal = [num for num in (seed + related) if isPalindrome(num)]
    return (totalCount, pal, seed, len(related))

totalCount, palindromicLychrel, lychrelSeeds, relatedCount = seedAndRelated()
print("[1..10,000] contains", totalCount, "Lychrel numbers.")
print(str(palindromicLychrel), "are palindromic Lychrel numbers.")
print(str(lychrelSeeds), "are Lychrel seeds.")
print("There are", relatedCount, "related Lychrel numbers.")
```