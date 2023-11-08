```python
def powerMod(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def main():
    base = 5
    exponent = 123456789
    mod = 1000000007
    result = powerMod(base, exponent, mod)
    print(result)

if __name__ == "__main__":
    main()
```