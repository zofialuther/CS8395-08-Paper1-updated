from collections import deque

class CalkinWilfSequence:

    @staticmethod
    def main():
        term = Rational(1, 1)
        print("First 20 terms of the Calkin-Wilf sequence are:")
        for i in range(1, 21):
            print("{:2}: {}".format(i, term))
            term = CalkinWilfSequence.nextCalkinWilf(term)
        print()

        rational = Rational(83_116, 51_639)
        print(" {} is the {}th term of the sequence.".format(rational, CalkinWilfSequence.termIndex(rational)))

    @staticmethod
    def nextCalkinWilf(aTerm):
        divisor = Rational(2, 1).multiply(aTerm.floor()).add(Rational(1, 1)).subtract(aTerm)
        return Rational(1, 1).divide(divisor)

    @staticmethod
    def termIndex(aRational):
        result = 0
        binaryDigit = 1
        power = 0
        for term in CalkinWilfSequence.continuedFraction(aRational):
            for i in range(term):
                power += 1
                result |= (binaryDigit << power)
            binaryDigit = 0 if binaryDigit == 1 else 1
        return result

    @staticmethod
    def continuedFraction(aRational):
        numerator = aRational.numerator()
        denominator = aRational.denominator()
        result = deque()

        while numerator != 1:
            result.append(numerator // denominator)
            copyNumerator = numerator
            numerator = denominator
            denominator = copyNumerator % denominator

        if result and len(result) % 2 == 0:
            back = result.pop()
            result.append(back - 1)
            result.append(1)
        return result

class Rational:

    def __init__(self, aNumerator, aDenominator):
        if aDenominator == 0:
            raise ArithmeticError("Denominator cannot be zero")
        if aNumerator == 0:
            aDenominator = 1
        if aDenominator < 0:
            self.numer = -aNumerator
            self.denom = -aDenominator
        else:
            self.numer = aNumerator
            self.denom = aDenominator
        gcd = self.gcd(self.numer, self.denom)
        self.numer //= gcd
        self.denom //= gcd

    def add(self, aOther):
        return Rational(self.numer * aOther.denom + aOther.numer * self.denom, self.denom * aOther.denom)

    def subtract(self, aOther):
        return Rational(self.numer * aOther.denom - aOther.numer * self.denom, self.denom * aOther.denom)

    def multiply(self, aOther):
        return Rational(self.numer * aOther.numer, self.denom * aOther.denom)

    def divide(self, aOther):
        return Rational(self.numer * aOther.denom, self.denom * aOther.numer)

    def floor(self):
        return Rational(self.numer // self.denom, 1)

    def numerator(self):
        return self.numer

    def denominator(self):
        return self.denom

    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)

    ONE = Rational(1, 1)
    TWO = Rational(2, 1)

    def gcd(self, aOne, aTwo):
        if aTwo == 0:
            return aOne
        return self.gcd(aTwo, aOne % aTwo)