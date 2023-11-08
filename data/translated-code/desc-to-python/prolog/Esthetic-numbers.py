```python
def is_esthetic_number(num, base):
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    return all(digits[i] <= digits[i+1] for i in range(len(digits)-1))

def print_esthetic_numbers_in_base(base, start, end):
    for num in range(start, end+1):
        if is_esthetic_number(num, base):
            print(num, end=", ")
    print()

def find_next_esthetic_number(base, start):
    num = start + 1
    while not is_esthetic_number(num, base):
        num += 1
    return num

# Main predicate
def main():
    print("Esthetic numbers in base 2 from 1 to 20:")
    print_esthetic_numbers_in_base(2, 1, 20)
    print("Next esthetic number in base 3 after 20:", find_next_esthetic_number(3, 20))

if __name__ == "__main__":
    main()
```