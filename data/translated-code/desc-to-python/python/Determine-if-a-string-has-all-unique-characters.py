```python
def duplicatedCharIndices(s):
    seen = {}
    for i, char in enumerate(s):
        if char in seen:
            return (char, [seen[char], i])
        seen[char] = i
    return "Nothing"

def main():
    test_strings = ["abcdefg", "hello", "python", "programming"]
    for test in test_strings:
        result = duplicatedCharIndices(test)
        print(f"String: {test}, Result: {result}")

if __name__ == "__main__":
    main()
```