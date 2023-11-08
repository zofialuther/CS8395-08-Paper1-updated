```python
from Data.List import unfoldr

def binaryDigits(num):
    binary = unfoldr(lambda x: None if x == 0 else (x % 2, x // 2), num)
    return ''.join(map(str, binary[::-1]))

def main():
    test_numbers = [5, 10, 15]
    for num in test_numbers:
        print(binaryDigits(num))

if __name__ == "__main__":
    main()
```