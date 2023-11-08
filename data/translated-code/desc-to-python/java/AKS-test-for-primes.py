```python
# Python code implementing the AKS primality test

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def polynomial_expression(n):
    coefficients = [1]
    for i in range(1, n):
        new_coefficients = [1]
        for j in range(1, i):
            new_coefficients.append(coefficients[j-1] + coefficients[j])
        new_coefficients.append(1)
        coefficients = new_coefficients
    return coefficients

def aks_primality_test(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    coefficients = polynomial_expression(n)
    for a in range(2, int(n**0.5) + 1):
        if n % a == 0 and (a**n) % n != a:
            return False
        if coefficients[a] % n != 0:
            return False
    return True

def main():
    count = 0
    num = 2
    while count < 10:
        if aks_primality_test(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    main()
```