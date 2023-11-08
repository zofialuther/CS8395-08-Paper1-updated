import Data.Numbers.Primes

def attractiveNumbers():
    return list(filter(lambda x: isPrime(len(primeFactors(x))), range(1, 1000)))

def main():
    result = list(takeWhile(lambda x: x <= 120, attractiveNumbers()))
    print(result)