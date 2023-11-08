```python
from __future__ import print_function

def reverse_and_add(n):
    return n + int(str(n)[::-1])

def split_root(n):
    for i in range(1, len(str(n))):
        yield int(str(n)[:i]), int(str(n)[i:])

def is_lychrel(n, limit):
    for i in range(limit):
        n = reverse_and_add(n)
        if str(n) == str(n)[::-1]:
            return False
    return True

def find_lychrel_numbers(start, end, limit):
    lychrel_numbers = []
    related_lychrel_numbers = 0
    lychrel_palindromes = []

    for num in range(start, end+1):
        if is_lychrel(num, limit):
            lychrel_numbers.append(num)
            roots = list(split_root(num))
            if all(is_lychrel(root, limit) for root in roots):
                related_lychrel_numbers += 1
                if str(num) == str(num)[::-1]:
                    lychrel_palindromes.append(num)

    print("Number of Lychrel numbers:", len(lychrel_numbers))
    print("Lychrel numbers:", lychrel_numbers)
    print("Number of related Lychrel numbers:", related_lychrel_numbers)
    print("Lychrel palindromes:", lychrel_palindromes)

find_lychrel_numbers(1, 1000, 500)
```