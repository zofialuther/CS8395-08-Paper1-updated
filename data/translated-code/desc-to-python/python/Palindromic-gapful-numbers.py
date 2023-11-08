```python
import itertools
import pprint
import re
import heapq

def is_gapful(num):
    num_str = str(num)
    if len(num_str) < 3:
        return False
    gapful_num = int(num_str[0] + num_str[-1])
    return num % gapful_num == 0

def generate_palindrome_numbers():
    for i in itertools.count(1):
        yield int(str(i) + str(i)[-2::-1])

def main(m, n):
    palindromes = generate_palindrome_numbers()
    gapful_numbers = heapq.nsmallest(m, (num for num in palindromes if is_gapful(num)))
    last_digit_bins = {}
    for num in gapful_numbers:
        last_digit = num % 10
        if last_digit not in last_digit_bins:
            last_digit_bins[last_digit] = []
        last_digit_bins[last_digit].append(num)
    pprint.pprint({k: last_digit_bins[k][-n:] for k in sorted(last_digit_bins)})
    
if __name__ == "__main__":
    main(100, 10)
```