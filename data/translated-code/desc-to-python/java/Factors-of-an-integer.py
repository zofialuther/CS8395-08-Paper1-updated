def calculate_factors(num):
    factors = set()
    factors.add(1)
    factors.add(num)
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    
    return factors