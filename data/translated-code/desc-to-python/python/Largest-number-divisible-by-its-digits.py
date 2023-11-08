```python
from itertools import permutations
from functools import reduce
from math import gcd

def concatenate_digits(num_list):
    return int(''.join(map(str, num_list)))

def delete_element(num_list, index):
    del num_list[index]
    return num_list

def lcm(x, y):
    return x * y // gcd(x, y)

def find_largest_divisible_number():
    digits = [1, 2, 3, 4, 6, 7, 8, 9]
    lcm_of_digits = reduce(lcm, digits)
    max_num = 0
    for perm in permutations(digits, 7):
        for i in range(7):
            num = concatenate_digits(delete_element(perm, i))
            if num % lcm_of_digits == 0 and num > max_num:
                max_num = num
    print(max_num)

find_largest_divisible_number()
```