```python
def f1(x):
    return x * 2

def f2(x):
    return x ** 2

def main():
    numbers = [1, 2, 3, 4, 5]
    results_f1 = list(map(f1, numbers))
    results_f2 = list(map(f2, numbers))
    print("Results of applying f1 to numbers:", results_f1)
    print("Results of applying f2 to numbers:", results_f2)

main()
```