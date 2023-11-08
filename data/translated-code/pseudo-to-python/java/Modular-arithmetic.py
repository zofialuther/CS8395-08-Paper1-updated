class ModularArithmetic:
    class Ring:
        def plus(self, rhs):
            pass

        def times(self, rhs):
            pass

        def value(self):
            pass

        def one(self):
            pass

        def pow(self, p):
            if p < 0:
                raise ValueError("p must be zero or greater")
            pp = p
            pwr = self.one()
            while pp > 0:
                pwr = pwr.times(self)
                pp -= 1
            return pwr

    class ModInt(Ring):
        def __init__(self, value, modulo):
            self.value = value
            self.modulo = modulo

        def plus(self, other):
            if not isinstance(other, ModularArithmetic.ModInt):
                raise ValueError("Cannot add an unknown ring.")
            rhs = other
            if self.modulo != rhs.modulo:
                raise ValueError("Cannot add rings with different modulus")
            return ModularArithmetic.ModInt((self.value + rhs.value) % self.modulo, self.modulo)

        def times(self, other):
            if not isinstance(other, ModularArithmetic.ModInt):
                raise ValueError("Cannot multiply an unknown ring.")
            rhs = other
            if self.modulo != rhs.modulo:
                raise ValueError("Cannot multiply rings with different modulus")
            return ModularArithmetic.ModInt((self.value * rhs.value) % self.modulo, self.modulo)

        def value(self):
            return self.value

        def one(self):
            return ModularArithmetic.ModInt(1, self.modulo)

        def __str__(self):
            return "ModInt({}, {})".format(self.value, self.modulo)

    def f(self, x):
        return x.pow(100).plus(x).plus(x.one())

    def main(self, args):
        x = ModularArithmetic.ModInt(10, 13)
        y = self.f(x)
        print("x ^ 100 + x + 1 for x = ModInt(10, 13) is ")
        print(y)

mod = ModularArithmetic()
mod.main([])