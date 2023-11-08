```python
import math
import sympy

class SemiPrime:
    @staticmethod
    def primeDecomp(num):
        factors = []
        for i in range(2, int(math.sqrt(num)) + 1):
            while num % i == 0:
                factors.append(i)
                num = num // i
        if num > 1:
            factors.append(num)
        return factors

    @staticmethod
    def isSemi(num):
        factors = SemiPrime.primeDecomp(num)
        return len(factors) == 2 and factors[0] != factors[1]

if __name__ == "__main__":
    semi_primes_2_to_100 = [num for num in range(2, 101) if SemiPrime.isSemi(num)]
    semi_primes_1675_to_1680 = [num for num in range(1675, 1681) if SemiPrime.isSemi(num)]
    print("Semi-prime numbers between 2 and 100:", semi_primes_2_to_100)
    print("Semi-prime numbers between 1675 and 1680:", semi_primes_1675_to_1680)
```