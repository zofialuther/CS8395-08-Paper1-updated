from fractions import Fraction

class BigRational:
    @staticmethod
    def valueOf(num):
        return Fraction(num)

    ONE = Fraction(1)

    def reciprocal(self):
        return 1 / self

    def add(self, other):
        return self + other

if __name__ == "__main__":
    MAX_NUM = 1 << 19
    print(f"Searching for perfect numbers in the range [1, {MAX_NUM - 1}]")

    TWO = BigRational.valueOf(2)
    for i in range(1, MAX_NUM):
        reciprocalSum = BigRational.ONE
        if i > 1:
            reciprocalSum = reciprocalSum.add(BigRational.valueOf(i).reciprocal())
        maxDivisor = int(i ** 0.5)
        if maxDivisor >= i:
            maxDivisor -= 1

        for divisor in range(2, maxDivisor + 1):
            if i % divisor == 0:
                reciprocalSum = reciprocalSum.add(BigRational.valueOf(divisor).reciprocal())
                dividend = i // divisor
                if divisor != dividend:
                    reciprocalSum = reciprocalSum.add(BigRational.valueOf(dividend).reciprocal())
        
        if reciprocalSum == TWO:
            print(str(i) + " is a perfect number")