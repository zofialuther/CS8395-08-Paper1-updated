def calculate_nth_root(n, x):
    if n <= 1 or x <= 0:
        return "Invalid input parameters"
    
    guess = x / 2.0
    precision = 0.0001
    
    def iter(guess, n, x):
        return ((n - 1) * guess + x / (guess ** (n-1))) / n
    
    while abs(guess**n - x) > precision:
        guess = iter(guess, n, x)
    
    return guess