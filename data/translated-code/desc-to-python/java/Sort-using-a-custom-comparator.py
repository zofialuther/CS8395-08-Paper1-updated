```python
class Test:
    def main():
        arr = ["apple", "banana", "Orange", "grape", "kiwi"]
        arr.sort(key=lambda x: (-len(x), x.lower()))
        for s in arr:
            print(s)
```