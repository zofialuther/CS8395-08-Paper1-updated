```python
import random
from math import isqrt

class RabinMillerPrimalityTest:
    
    @staticmethod
    def isPrime(n, precision=20):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        
        for _ in range(precision):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True

    @staticmethod
    def isPrimeBigInteger(number, precision=20):
        return RabinMillerPrimalityTest.isPrime(number, precision)

    @staticmethod
    def isPrimeInt(number, precision=20):
        return RabinMillerPrimalityTest.isPrime(number, precision)

    @staticmethod
    def isPrimeLong(number, precision=20):
        return RabinMillerPrimalityTest.isPrime(number, precision)
```