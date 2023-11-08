```python
import math

def print_triangle(n):
    print(f"{n} rows:")
    rowNum = 1
    printMe = 1
    numsPrinted = 0
    while rowNum <= n:
        cols = math.ceil(math.log10(n*(n-1)//2 + numsPrinted + 2))
        print(f"%{cols}d " % printMe, end='')
        numsPrinted += 1
        if numsPrinted == rowNum:
            print()
            rowNum += 1
            numsPrinted = 0
        printMe += 1

def main():
    print_triangle(5)
    print_triangle(14)

if __name__ == "__main__":
    main()
```