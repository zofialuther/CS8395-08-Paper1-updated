```python
from typing import Union

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modInv(a: int, m: int) -> Union[int, None]:
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def main():
    result1 = modInv(3, 11)
    result2 = modInv(5, 12)
    print(result1)  # Output: 4
    print(result2)  # Output: None

main()
```