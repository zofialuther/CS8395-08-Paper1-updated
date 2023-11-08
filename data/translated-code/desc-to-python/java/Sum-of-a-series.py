```python
def f(x):
    return 1/(x*x)

def main():
    start = 1
    end = 1000
    total_sum = 0
    for x in range(start, end+1):
        total_sum += f(x)
    print("The sum of f(x) for the range", start, "to", end, "is", total_sum)

main()
```