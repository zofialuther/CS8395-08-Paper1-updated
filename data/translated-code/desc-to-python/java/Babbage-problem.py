```python
class Test:
    def main(self):
        n = 0
        while True:
            n += 1
            if (n ** 2) % 1000000 == 269696:
                break
        print(n)
```