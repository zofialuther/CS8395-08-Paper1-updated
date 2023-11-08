```python
def a(i):
    return i

def b(j):
    return j

for i in (False, True):
    for j in (False, True):
        print("\nCalculating: x = a(i) and b(j) using x = b(j) if a(i) else False")
        x = b(j) if a(i) else False
        print("Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True")
        y = b(j) if not a(i) else True
        print(f"  # Called function a({i}) -> {a(i)}")
        print(f"  # Called function b({j}) -> {b(j)}")
```