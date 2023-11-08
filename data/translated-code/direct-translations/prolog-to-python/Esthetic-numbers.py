```python
def main():
    for base in range(2, 17):
        min_index = base * 4
        max_index = base * 6
        print_esthetic_numbers1(base, min_index, max_index)
    
    print_esthetic_numbers2(1000, 9999, 16)
    print()
    print_esthetic_numbers2(100000000, 130000000, 8)

def print_esthetic_numbers1(base, min_index, max_index):
    format_str = f'\n{base} '
    print(f'Esthetic numbers in base {base} from index {min_index} through index {max_index}:\n')
    print_esthetic_numbers1_helper(base, format_str, min_index, max_index, 0, 1)

def print_esthetic_numbers1_helper(base, format_str, min_index, max_index, m, i):
    if i <= max_index:
        next_num = next_esthetic_number(base, m)
        if i >= min_index:
            print(format_str % next_num, end='')
        j = i + 1
        print_esthetic_numbers1_helper(base, format_str, min_index, max_index, next_num, j)
    else:
        print('\n\n')

def print_esthetic_numbers2(min_val, max_val, per_line):
    print(f'Esthetic numbers in base 10 between {min_val} and {max_val}:\n')
    m = min_val - 1
    print_esthetic_numbers2_helper(max_val, per_line, m, 0)

def print_esthetic_numbers2_helper(max_val, per_line, m, count):
    next_num = next_esthetic_number(10, m)
    if next_num <= max_val:
        print(next_num, end=' ')
        count += 1
        if count % per_line == 0:
            print()
        print_esthetic_numbers2_helper(max_val, per_line, next_num, count)
    else:
        print(f'\nCount: {count}')

def next_esthetic_number(base, m):
    n = m + 1
    if n < base:
        return n
    else:
        a = m // base
        b = a % base
        if b == m % base + 1 and b + 1 < base:
            return m + 2
        else:
            c = next_esthetic_number(base, a)
            d = c % base
            if d == 0:
                e = 1
            else:
                e = d - 1
            return c * base + e

main()
```