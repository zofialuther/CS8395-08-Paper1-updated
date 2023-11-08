```python
import threading

def genfactors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def primedecomp(num):
    factors = genfactors(num)
    prime_factors = []
    for factor in factors:
        if len(genfactors(factor)) == 2:
            prime_factors.append(factor)
    return prime_factors

def main(A):
    result = {}
    
    def calculate_prime_factors(num):
        result[num] = primedecomp(num)
    
    threads = []
    for num in A:
        t = threading.Thread(target=calculate_prime_factors, args=(num,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    max_min_factor_element = max(result, key=lambda x: min(result[x]))
    print("Element:", max_min_factor_element, "Prime Factor Decomposition:", result[max_min_factor_element])

A = [12, 15, 20, 30, 36]
main(A)
```