def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def min_mult_dsum(n, multiple):
    if digit_sum(n) == digit_sum(n * multiple):
        return n * multiple
    else:
        return min_mult_dsum(n, multiple + 1)

def main():
    for n in range(1, 41):
        result = min_mult_dsum(n, 2)
        print(f"The minimum multiple of {n} with the same digit sum is: {result}")

main()