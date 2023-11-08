```python
fusc_cache = {}

def fusc(n):
    if n in fusc_cache:
        return fusc_cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n % 2 == 0:
        result = fusc(n // 2)
    else:
        result = fusc((n - 1) // 2) + fusc((n + 1) // 2)
    fusc_cache[n] = result
    return result

def print_first_n_fusc_numbers(n):
    for i in range(n):
        print(fusc(i))

def print_longest_fusc_numbers_up_to_limit(limit):
    longest_length = 0
    for i in range(limit+1):
        fusc_num = fusc(i)
        if len(str(fusc_num)) > longest_length:
            longest_length = len(str(fusc_num))
            print(fusc_num)

def main():
    print_first_n_fusc_numbers(10)
    print_longest_fusc_numbers_up_to_limit(100)

if __name__ == "__main__":
    main()
```