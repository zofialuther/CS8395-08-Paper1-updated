from math import log10

def generate_fibonacci(n):
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def main():
    numbers = generate_fibonacci(1000)
    
    first_digits = [0] * 10
    for number in numbers:
        first_digits[int(str(number)[0])] += 1
    
    for i in range(1, len(first_digits)):
        print("%d %10.6f %10.6f" % (i, first_digits[i] / len(numbers), log10(1.0 + 1.0 / i)))

if __name__ == "__main__":
    main()