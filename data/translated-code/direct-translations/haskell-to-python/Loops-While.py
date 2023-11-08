```
def loop(n):
    if n > 0:
        print(n)
        loop(n // 2)

loop(1024)
```