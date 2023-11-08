```python
import time
import resource

def factorsO(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

numbers = [120, 12041111117]

for number in numbers:
    start_time = time.time()
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    factors = factorsO(number)
    end_time = time.time()
    end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    print(f"Factors of {number}: {factors}")
    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Memory used: {end_mem - start_mem} bytes")
```