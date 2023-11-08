def pow(base, exp):
    if exp < 0:
        return 1 / pow(base, -exp)
    ans = 1.0
    for _ in range(exp):
        ans *= base
    return ans

print(pow(2, 30))
print(pow(2.0, 30))  # tests
print(pow(2.0, -2))