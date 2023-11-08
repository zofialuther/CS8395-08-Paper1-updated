```python
def collapse(s):
    result = []
    for char in s:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

def main():
    example_strings = ["hello", "mississippi", "aaaaa", "abcde"]
    for s in example_strings:
        collapsed = collapse(s)
        print(f"Original: {s}, Collapsed: {collapsed}")

if __name__ == "__main__":
    main()
```