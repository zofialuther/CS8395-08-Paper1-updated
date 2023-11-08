```python
from collections import Counter

def report_duplicates(S):
    duplicates = [char for char, count in Counter(S).items() if count > 1]
    if duplicates:
        report(duplicates)
    else:
        print("No duplicate characters found")

def report(duplicates):
    for char in duplicates:
        positions = [i for i, letter in enumerate(S) if letter == char]
        print(f"Character '{char}' appears at positions {positions}")

def test():
    test_strings = ["hello", "world", "python", "programming"]
    for string in test_strings:
        print(f"Testing string: {string}")
        report_duplicates(string)
        print("-" * 30)

test()
```