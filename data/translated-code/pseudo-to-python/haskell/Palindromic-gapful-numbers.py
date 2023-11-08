```python
import math

def gapful(n):
    if n % int(str(n)[0] + str(n)[-1]) == 0:
        return True
    else:
        return False

def firstLastDigit(n):
    return int(str(n)[-1] + str(n)[0])

def toPalindrome(n):
    return str(n) == str(n)[::-1]

def go(p, n):
    if n == 0:
        return p
    else:
        return go(p, n-1)

def gapfulPalindromes():
    palindromes = [i for i in range(1, 100000) if toPalindrome(i)]
    gapful_palindromes = list(filter(lambda x: x > 100 and gapful(x), palindromes))
    return sorted(gapful_palindromes)

def endsWith(n):
    return list(filter(lambda x: x % 10 == n, gapfulPalindromes()))

def showSets(k, r):
    result = k + " description\n" + "\n".join(map(str, r(range(1, 10))))
    return result

def main():
    sets = [("set1", endsWith), ("set2", endsWith)]
    for s in sets:
        print(showSets(s[0], s[1]))

main()
```