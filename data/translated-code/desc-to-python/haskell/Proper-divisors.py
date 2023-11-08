```python
import sympy
import operator

def find_proper_divisors(num):
    divisors = [1]
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def display_divisor_table(start, end):
    for i in range(start, end+1):
        divisors = find_proper_divisors(i)
        print(f"Proper divisors of {i}: {divisors}")

def main():
    display_divisor_table(1, 10)
    
    max_divisor_count = 0
    number_with_max_divisors = 0
    for i in range(1, 20001):
        divisors = find_proper_divisors(i)
        if len(divisors) > max_divisor_count:
            max_divisor_count = len(divisors)
            number_with_max_divisors = i
    
    print(f"The number with the most proper divisors is {number_with_max_divisors} with {max_divisor_count} divisors.")

if __name__ == "__main__":
    main()
```