```python
def isHappy(n):
    def p(s, n):
        if n == 1:
            return True
        if n in s:
            return False
        else:
            s.add(n)
            return p(s, f(n))
    
    def f(n):
        return sum(int(digit)**2 for digit in str(n))
    
    return p(set(), n)

if __name__ == "__main__":
    results = []
    num = 1
    while len(results) < 8:
        if isHappy(num):
            results.append(num)
        num += 1
    print(results)
```