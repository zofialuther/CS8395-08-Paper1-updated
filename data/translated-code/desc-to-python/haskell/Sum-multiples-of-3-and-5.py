```python
def sum35(num):
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def sumMulS(*args):
    total = 0
    for num in args:
        total += sum35(num)
    return total

def pairLCM(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

def main():
    print(sum35(10))
    print(sumMulS(10, 20, 30))
    print(pairLCM(15, 20))

if __name__ == "__main__":
    main()
```