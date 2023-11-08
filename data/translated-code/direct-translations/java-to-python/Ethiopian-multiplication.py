```python
def doubleInt(doubleMe):
    return doubleMe << 1  # shift left

def halveInt(halveMe):
    return halveMe >> 1  # shift right

def isEven(num):
    return (num & 1) == 0

def main():
    first = int(input())
    second = int(input())

    if first < 0:
        first = -first
        second = -second

    columns = {}
    columns[first] = second
    sum = 0 if isEven(first) else second
    while first > 1:
        first = halveInt(first)
        second = doubleInt(second)
        columns[first] = second
        if not isEven(first):
            sum += second

    print(sum)

if __name__ == "__main__":
    main()
```