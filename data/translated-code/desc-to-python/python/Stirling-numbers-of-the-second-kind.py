def sterling2(n, k, memo={}):
    if k == 0 or n == 0 or k > n:
        return 0
    if k == 1 or k == n:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    result = k * sterling2(n-1, k, memo) + sterling2(n-1, k-1, memo)
    memo[(n, k)] = result
    return result

max_value = 0
for k in range(1, 101):
    value = sterling2(100, k)
    if value > max_value:
        max_value = value

num_digits = len(str(max_value))

print("Maximum value of S2(100, k):", max_value)
print("Number of digits in maximum value:", num_digits)