```python
class AksTest:
    c = [0] * 64

    @staticmethod
    def main(args):
        for n in range(10):
            AksTest.coeff(n)
            AksTest.show(n)

        print("Primes:", end="")
        for n in range(1, len(AksTest.c)):
            if AksTest.is_prime(n):
                print(" ", n, end="")

        print()

    @staticmethod
    def coeff(n):
        AksTest.c[0] = 1
        for i in range(n):
            AksTest.c[0] = -AksTest.c[0]
            AksTest.c[i + 1] = 1
            for j in range(i, 0, -1):
                AksTest.c[j] = AksTest.c[j - 1] - AksTest.c[j]

    @staticmethod
    def is_prime(n):
        AksTest.coeff(n)
        AksTest.c[0] += 1
        AksTest.c[n] -= 1
        i = n
        while i != 0 and AksTest.c[i] % n == 0:
            i -= 1
        return i < 0

    @staticmethod
    def show(n):
        print("(x-1)^" + str(n) + " =", end="")
        for i in range(n, -1, -1):
            print(" + " + str(AksTest.c[i]) + "x^" + str(i), end="")
        print()
```