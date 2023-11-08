```python
def tween(N):
    return 11 <= N % 100 <= 13

def nth(N):
    if tween(N):
        return str(N) + "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(N % 10, "th")
        return str(N) + suffix

def test():
    for i in range(1, 21):
        print(nth(i))

test()
```