```python
import threading
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def threaded_decomp(n, result):
    result.append((n, factorize(n)))

def threaded_decomp_list(numbers):
    results = []
    threads = []
    for num in numbers:
        result = []
        thread = threading.Thread(target=threaded_decomp, args=(num, result))
        threads.append(thread)
        thread.start()
        results.append(result)
    for thread in threads:
        thread.join()
    return results

def pack_exit_out(results):
    return [item for sublist in results for item in sublist]

def largest_min_factor(results):
    min_factors = [min(factors) for _, factors in results]
    return max(min_factors)

def format_it(result):
    print(result)

# Example usage:
numbers = [24, 36, 48, 60]
results = threaded_decomp_list(numbers)
packed_results = pack_exit_out(results)
largest_factor = largest_min_factor(packed_results)
format_it(largest_factor)
```