def isSemiprime(n):
    factors = primeFactors(n)
    if (len(factors) == 2 and (factors[0] * factors[1] == n)) or (len(factors) == 1 and (factors[0] ** 2 == n)):
        return True
    else:
        return False