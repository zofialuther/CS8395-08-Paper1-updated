```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def m_factor(exponent):
    mersenne_number = 2 ** exponent - 1
    for i in range(2, int(mersenne_number ** 0.5) + 1):
        if mersenne_number % i == 0:
            return i
    return None

def main():
    exponent = int(input("Enter the exponent of a Mersenne number: "))
    if is_prime(exponent):
        factor = m_factor(exponent)
        if factor:
            print(f"A factor of the Mersenne number is {factor}.")
        else:
            print("No factor found for the Mersenne number.")
    else:
        print("The exponent is not prime.")

main()
```