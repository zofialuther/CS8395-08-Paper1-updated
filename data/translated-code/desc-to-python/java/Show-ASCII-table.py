```python
def showAsciiTable():
    for i in range(32, 128):
        if i % 6 == 0:
            print()
        if i == 32:
            print(f"{i:<3} {'Space':<5}", end=" ")
        elif i == 127:
            print(f"{i:<3} {'Delete':<5}", end=" ")
        else:
            print(f"{i:<3} {chr(i):<5}", end=" ")
```