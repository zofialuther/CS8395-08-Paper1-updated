def isSemiprime(num):
    factors = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    if num > 1:
        factors.append(num)
    if len(factors) == 2 and factors[0] * factors[1] == num:
        return True
    elif len(factors) == 1 and factors[0] * factors[0] == num:
        return True
    else:
        return False