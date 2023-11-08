from fractions import Fraction
from math import gcd

class EgyptianFractions:
    @staticmethod
    def to_egyptian(nr, dr):
        denoms = []
        while nr != 0:
            d = -(-dr // nr)  # ceiling division
            denoms.append(d)
            nr, dr = dr % nr, dr * d
        return denoms

    @staticmethod
    def main():
        fracs = [
            Fraction(43, 48),
            Fraction(5, 121),
            Fraction(2014, 59)
        ]

        for frac in fracs:
            egyptian = EgyptianFractions.to_egyptian(frac.numerator, frac.denominator)
            print(f"{frac} -> {' + '.join(f'1/{d}' for d in egyptian)}")

        for r in [98, 998]:
            print(f"\nFor proper fractions with 1 or 2 digits:" if r == 98 else
                  f"\nFor proper fractions with 1, 2 or 3 digits:")

            maxSize = 0
            maxSizeFracs = []
            maxDen = 0
            maxDenFracs = []
            sieve = [[False] * (r + 2) for _ in range(r + 1)]
            for i in range(1, r):
                for j in range(i + 1, r + 1):
                    if sieve[i][j]:
                        continue
                    egyptian = EgyptianFractions.to_egyptian(i, j)
                    listSize = len(egyptian)
                    if listSize > maxSize:
                        maxSize = listSize
                        maxSizeFracs = [Fraction(i, j)]
                    elif listSize == maxSize:
                        maxSizeFracs.append(Fraction(i, j))
                    listDen = egyptian[-1]
                    if listDen > maxDen:
                        maxDen = listDen
                        maxDenFracs = [Fraction(i, j)]
                    elif listDen == maxDen:
                        maxDenFracs.append(Fraction(i, j))
                    if i < r // 2:
                        k = 2
                        while j * k <= r + 1:
                            sieve[i * k][j * k] = True
                            k += 1
            print(f"  largest number of items = {maxSize}")
            print(f"fraction(s) with this number : {maxSizeFracs}")
            print(f"  largest denominator = {len(str(maxDen))} digits, {str(maxDen)[:20]}...{str(maxDen)[-20:]}")
            print(f"fraction(s) with this denominator : {maxDenFracs}")


if __name__ == "__main__":
    EgyptianFractions.main()