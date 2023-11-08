import fractions
import itertools

def continued_fraction_sqrt2(terms):
    frac = fractions.Fraction(1, 2)
    for _ in range(terms):
        yield 1
        yield frac

def continued_fraction_e(terms):
    yield 2
    for k in itertools.count(2, 2):
        yield 1
        yield k

def continued_fraction_pi(terms):
    for k in itertools.count(1):
        yield 2 if k % 2 == 1 else 1
        yield 1
        yield 2 * k

def approx_cont_frac(cf):
    num = 0
    den = 1
    for term in cf:
        num, den = den, term * den + num
    return num, den

def main():
    terms = 10
    print("Square root of 2:", approx_cont_frac(continued_fraction_sqrt2(terms)))
    print("Napier's Constant (e):", approx_cont_frac(continued_fraction_e(terms)))
    print("Pi:", approx_cont_frac(continued_fraction_pi(terms)))

main()