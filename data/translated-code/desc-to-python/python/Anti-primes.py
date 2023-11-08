```python
def factors(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return result

def antiprimes(limit):
    n = 1
    while True:
        if len(factors(n)) > limit:
            yield n
        n += 1

count = 0
for num in antiprimes(40):
    print(num)
    count += 1
    if count == 40:
        break
```