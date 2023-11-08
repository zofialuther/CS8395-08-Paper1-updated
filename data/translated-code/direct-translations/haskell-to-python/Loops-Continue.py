```python
def out(x):
    if x % 5 == 0:
        print(x)
    else:
        print(x, end=", ")

for x in range(1, 11):
    out(x)
```