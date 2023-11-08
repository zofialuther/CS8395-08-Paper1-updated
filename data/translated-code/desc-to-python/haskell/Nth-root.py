def nthRoot(number, n):
    guess = number / 2
    while abs(guess ** n - number) > 0.0001:
        guess = guess - (guess ** n - number) / (n * (guess ** (n-1)))
    return guess