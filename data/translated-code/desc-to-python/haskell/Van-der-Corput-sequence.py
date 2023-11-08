```python
def digit_to_number(digit, base):
    return int(digit, base)

def number_to_digit(number, base):
    return np.base_repr(number, base)

def van_der_corput_sequence(n, base):
    sequence = []
    for i in range(1, n+1):
        number = i
        result = 0
        fraction = 1 / base
        while number > 0:
            result += (number % base) * fraction
            number //= base
            fraction /= base
        sequence.append(result)
    return sequence

def print_van_der_corput_range(start, end, base):
    for i in range(start, end+1):
        print(van_der_corput_sequence(i, base))

def main():
    print("Van der Corput numbers for base 2:")
    print_van_der_corput_range(1, 5, 2)
    print("Van der Corput numbers for base 10:")
    print_van_der_corput_range(1, 5, 10)
    print("Van der Corput numbers for base 123:")
    print_van_der_corput_range(1, 5, 123)

if __name__ == "__main__":
    main()
```