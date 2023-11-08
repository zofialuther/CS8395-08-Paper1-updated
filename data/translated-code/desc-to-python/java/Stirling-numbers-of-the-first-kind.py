```python
def stirling_numbers(n, k, memo={}):
    if k == 0 or n == 0:
        return 0
    if (n, k) in memo:
        return memo[(n, k)]
    if n == 1 and k == 1:
        return 1
    if k > n:
        return 0
    result = (n-1) * stirling_numbers(n-1, k, memo) + stirling_numbers(n-1, k-1, memo)
    memo[(n, k)] = result
    return result

max_value = 0
max_k = 0
for k in range(1, 101):
    result = stirling_numbers(100, k)
    if result > max_value:
        max_value = result
        max_k = k

print("Maximum value of S1(100, k):", max_value)
print("Number of digits:", len(str(max_value)))
print("Value of k:", max_k)
```