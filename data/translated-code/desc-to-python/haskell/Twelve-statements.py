```python
def tf(n):
    return [[i for i in range(1, n+1)]]

def wrongness(lst):
    return sum(lst)

def statements(lst):
    return [sum(lst) > 10, len(lst) == 5]

def testall(lst):
    return [statement(lst) for statement in statements(lst)]

def main():
    integers = [1, 2, 3, 4, 5]
    results = testall(integers)
    print(results)

if __name__ == "__main__":
    main()
```