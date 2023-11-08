```python
import Data.Map

def fstdigit(n):
    while n >= 10:
        n //= 10
    return n

def main():
    fib = [1, 1]
    while len(fib) < 100:
        fib.append(fib[-1] + fib[-2])
    
    digit_freq = Data.Map.fromListWith (+) [(fstdigit(x), 1) for x in fib]
    
    table = [(digit, freq, log(freq)) for (digit, freq) in Data.Map.toList(digit_freq)]
    
    for row in table:
        print(row)

if __name__ == "__main__":
    main()
```