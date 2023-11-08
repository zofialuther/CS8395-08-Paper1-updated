```python
def stirling_second(n, k, memo={}):
    if k == 0 or n == 0 or k > n:
        return 0
    if k == n:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    
    result = k * stirling_second(n-1, k, memo) + stirling_second(n-1, k-1, memo)
    memo[(n, k)] = result
    return result

def find_max_stirling(n):
    max_val = 0
    max_k = 0
    for k in range(1, n+1):
        val = stirling_second(n, k)
        if val > max_val:
            max_val = val
            max_k = k
    return max_val, len(str(max_val)), max_k

def print_stirling_table(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(stirling_second(i, j), end="\t")
        print()

n = 100
max_val, num_digits, max_k = find_max_stirling(n)
print("Maximum value of S2(100, k):", max_val)
print("Number of digits:", num_digits)
print("Value of k that resulted in the maximum:", max_k)

print("Stirling numbers table:")
print_stirling_table(10)
```