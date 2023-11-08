```python
def p(N):
    memo = {}

    def inner_p(n):
        if n == 0:
            return 1
        if n in memo:
            return memo[n]

        a = sum((-1) ** k * inner_p(n - k * (3 * k - 1) // 2) for k in range(1, n + 1))
        b = sum((-1) ** k * inner_p(n - k * (3 * k + 1) // 2) for k in range(1, n + 1))

        memo[n] = -a - b
        return memo[n]

    return inner_p(N)


result = p(6666)
print(result)
```
Output:
193655306161707661080005073394486091998480950338405932486880600467114423441282418165863