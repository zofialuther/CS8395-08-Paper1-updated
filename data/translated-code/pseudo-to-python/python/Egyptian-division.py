```python
import itertools

def egyptian_divmod(dividend, divisor):
    assert divisor != 0
    pwrs = [1]
    dbls = [divisor]
    while dbls[-1] <= dividend:
        pwrs.append(pwrs[-1] * 2)
        dbls.append(pwrs[-1] * divisor)
    ans = 0
    accum = 0
    for pwr, dbl in zip(pwrs[-2:], dbls[-2:]):
        if accum + dbl <= dividend:
            accum += dbl
            ans += pwr
    return ans, abs(accum - dividend)

if __name__ == "__main__":
    for i, j in itertools.product(range(13), range(1, 13)):
        assert egyptian_divmod(i, j) == divmod(i, j)
    i, j = 580, 34
    print("%i divided by %i using the Egyption method is %i remainder %i" % egyptian_divmod(i, j))
```