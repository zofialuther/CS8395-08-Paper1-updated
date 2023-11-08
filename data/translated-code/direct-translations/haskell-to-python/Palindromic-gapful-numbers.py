```python
from typing import List

def gapful(n: int) -> bool:
    def first_last_digit(x: int) -> int:
        return int(str(x)[0] + str(x)[-1])
    
    return n % first_last_digit(n) == 0

def to_palindrome(n: int) -> List[int]:
    def go(p: int, n: int) -> int:
        if n == 0:
            return p
        else:
            return go(p * 10 + (n % 10), n // 10)
    
    return list(filter(lambda x: x > 100 and gapful(x), [go(n, n), go(n, n // 10)]))

def gapful_palindromes() -> List[int]:
    return sorted([num for i in range(1, 100000) for num in to_palindrome(i)])

def ends_with(n: int) -> List[int]:
    return list(filter(lambda x: x % 10 == n, gapful_palindromes()))

def show_sets(k: str, r: callable) -> str:
    output = k + " palindromic gapful numbers ending in:\n"
    for i in range(1, 10):
        output += str(i) + ": " + str(r(ends_with(i))) + "\n"
    return output

def main() -> None:
    sets = [
        ("First 20", lambda x: x[:20]),
        ("Last 15 of first 100", lambda x: x[85:100]),
        ("Last 10 of first 1000", lambda x: x[990:1000])
    ]
    for k, r in sets:
        print(show_sets(k, r))

if __name__ == "__main__":
    main()
```