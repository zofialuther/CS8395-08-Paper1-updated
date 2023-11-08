```python
def dept(x):
    return x in range(1, 8)

def police(x):
    return x in [2, 4, 6]

def fire(x):
    return dept(x)

def san(x):
    return dept(x)

def assign(a, b, c):
    if police(a) and fire(b) and san(c) and a != b and a != c and b != c and 12 == a + b + c:
        return True
    else:
        return False

def main():
    print("P F S")
    for police, fire, sanitation in [(p, f, s) for p in range(1, 8) for f in range(1, 8) for s in range(1, 8)]:
        if assign(police, fire, sanitation):
            print(police, fire, sanitation)

main()
```