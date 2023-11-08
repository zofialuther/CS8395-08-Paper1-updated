```python
class Test:
    @staticmethod
    def mod(a, b):
        return a % b
    
    @staticmethod
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def main():
        for i in range(10):
            for j in range(10):
                if Test.isPrime(i) and Test.isPrime(j):
                    if Test.mod(i, j) == 0:
                        print(f"Combination of prime numbers: {i}, {j}")
```