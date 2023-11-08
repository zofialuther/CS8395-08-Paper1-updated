```python
from collections import defaultdict

def repeat(s, n):
    result = ""
    for _ in range(n):
        result += s
    return result

def main():
    repeated_string = repeat("ha", 5)
    print(repeated_string)

if __name__ == "__main__":
    main()
```