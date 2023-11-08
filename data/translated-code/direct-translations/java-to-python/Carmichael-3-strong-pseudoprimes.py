```python
class Test:
    @staticmethod
    def mod(n, m):
        return ((n % m) + m) % m

    @staticmethod
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        elif n < 2 or n % 2 == 0 or n % 3 == 0:
            return False
        div = 5
        inc = 2
        while div ** 2 <= n:
            if n % div == 0:
                return False
            div += inc
            inc = 6 - inc
        return True

    @staticmethod
    def main(args):
        for p in range(2, 62):
            if not Test.is_prime(p):
                continue
            for h3 in range(2, p):
                g = h3 + p
                for d in range(1, g):
                    if (g * (p - 1)) % d != 0 or Test.mod(-p * p, h3) != d % h3:
                        continue
                    q = 1 + (p - 1) * g / d
                    if not Test.is_prime(q):
                        continue
                    r = 1 + (p * q / h3)
                    if not Test.is_prime(r) or (q * r) % (p - 1) != 1:
                        continue
                    print(f"{p} x {q} x {r}")

Test.main([])
```