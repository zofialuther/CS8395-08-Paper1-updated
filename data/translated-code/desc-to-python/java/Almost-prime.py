```python
import math

class AlmostPrime:
    @staticmethod
    def kprime(n, k):
        count = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                count += 1
                n //= i
                if count > k:
                    return False
        if n > 1:
            count += 1
        return count == k

    @staticmethod
    def main():
        for k in range(1, 6):
            count = 0
            num = 2
            while count < 5:
                if AlmostPrime.kprime(num, k):
                    print(num)
                    count += 1
                num += 1

AlmostPrime.main()
```