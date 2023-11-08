```python
class Attractive:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def count_prime_factors(num):
        count = 0
        for i in range(2, num + 1):
            while num % i == 0:
                if Attractive.is_prime(i):
                    count += 1
                num = num / i
        return count

    @staticmethod
    def main(max_value):
        for i in range(2, max_value + 1):
            if Attractive.is_prime(Attractive.count_prime_factors(i)):
                print(i)
```