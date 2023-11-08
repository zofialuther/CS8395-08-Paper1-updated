```python
def lengthThenAZ(s):
    return (len(s), s)

def descLengthThenAZ(s):
    return (-len(s), s)

def main():
    sample_strings = ["apple", "banana", "orange", "grape", "pineapple"]
    print(sorted(sample_strings, key=lengthThenAZ))
    print(sorted(sample_strings, key=descLengthThenAZ))

main()
```