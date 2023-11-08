```python
def trial():
    pass

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def convert_to_int(num_list, radix, value=0):
    if not num_list:
        return value
    else:
        return convert_to_int(num_list[1:], radix, value * radix + num_list[0])

def generate_digits(n):
    if n == 0:
        return []
    else:
        return generate_digits(n-1) + [n]

def generate_combinations(digits, n):
    if n == 0:
        return [digits]
    else:
        result = []
        for i in range(len(digits)):
            rest = digits[:i] + digits[i+1:]
            result += [[digits[i]] + comb for comb in generate_combinations(rest, n-1)]
        return result

def precalculate_combinations(radix, length):
    digits = list(range(1, radix+1))
    skip = radix - length
    return generate_combinations(digits[skip:], length)

def is_divisible_by_lcm(num_list, lcm_value):
    number = convert_to_int(num_list, 10)
    return number % lcm_value == 0

def largest_divisible_by_all():
    for length in range(9, 0, -1):
        combs = precalculate_combinations(10, length)
        for comb in combs:
            lcm_value = 1
            for digit in comb:
                lcm_value = lcm(lcm_value, digit)
            for perm in permutations(comb):
                if is_divisible_by_lcm(perm, lcm_value):
                    return convert_to_int(perm, 10)

def largest_decimal_number():
    return largest_divisible_by_all()

def largest_hexadecimal_number():
    return hex(largest_divisible_by_all())
```