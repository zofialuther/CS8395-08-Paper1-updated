```python
# Python code to check whether Mersenne numbers are prime or not

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_mersenne(exponent):
    return 2 ** exponent - 1

def check_mersenne_primality(exponent):
    mersenne_number = factorize_mersenne(exponent)
    return is_prime(mersenne_number)

def main():
    for i in range(1, 51):
        if check_mersenne_primality(i):
            print(f"2^{i} - 1 is prime")
        else:
            print(f"2^{i} - 1 is not prime")
    
    if check_mersenne_primality(929):
        print("2^929 - 1 is prime")
    else:
        print("2^929 - 1 is not prime")

if __name__ == "__main__":
    main()
```