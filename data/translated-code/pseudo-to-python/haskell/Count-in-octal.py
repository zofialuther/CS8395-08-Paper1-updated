```python
from Numeric import showOct

def main() -> None:
    for i in range(1, 2**31 - 1):
        octal_representation = showOct(i)
        print(octal_representation)
```