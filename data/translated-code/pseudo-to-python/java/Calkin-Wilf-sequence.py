class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def floor(self):
        return self.numerator // self.denominator
    
    def add(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
    
    def subtract(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
    
    def multiply(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def divide(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

def main():
    term = Rational(1, 1)
    print("First 20 terms of the Calkin-Wilf sequence are:")
    for i in range(1, 21):
        print(f"{i}: {term}")
        term = nextCalkinWilf(term)
    print("")
    rational = Rational(83_116, 51_639)
    print(f"{rational} is the {termIndex(rational)}th term of the sequence.")

def nextCalkinWilf(aTerm):
    divisor = Rational(2, 1).multiply(aTerm.floor()).add(Rational(1, 1)).subtract(aTerm)
    return Rational(1, 1).divide(divisor)

def termIndex(aRational):
    result = 0
    binaryDigit = 1
    power = 0
    for term in continuedFraction(aRational):
        for i in range(0, term):
            result |= (binaryDigit << power)
            power = power + 1
        binaryDigit = 1 if binaryDigit == 0 else 0
    return result

def continuedFraction(aRational):
    numerator = aRational.numerator
    denominator = aRational.denominator
    result = []
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

main()