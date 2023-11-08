```python
def divcount(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    return count

def antiprimes(N):
    result = []
    current_num = 1
    while len(result) < N:
        if divcount(current_num) > max(divcount(i) for i in range(1, current_num)):
            result.append(current_num)
        current_num += 1
    return result

def main():
    print(antiprimes(20))

main()
```