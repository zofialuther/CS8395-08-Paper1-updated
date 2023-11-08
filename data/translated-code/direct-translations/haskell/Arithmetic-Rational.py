from fractions import Fraction

# Prints the first N perfect numbers
def main():
    n = 4
    perfect_numbers = [candidate for candidate in range(2, 2**19) if get_sum(candidate) == 1]
    for number in perfect_numbers[:n]:
        print(number)

def get_sum(candidate):
    return Fraction(1, candidate) + sum([Fraction(1, factor) + Fraction(1, candidate // factor) for factor in range(2, int(candidate**0.5) + 1) if candidate % factor == 0])

main()