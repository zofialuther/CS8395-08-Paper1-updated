from math import gcd

class Triples:
    LIMIT = 0
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    primCount = 0
    tripCount = 0
    
    @staticmethod
    def parChild(a, b, c):
        perim = a + b + c
        if perim > Triples.LIMIT:
            return
        Triples.primCount += 1
        Triples.tripCount += Triples.LIMIT // perim
        a2, b2, c2, c3 = 2*a, 2*b, 2*c, 3*c
        Triples.parChild(a - b2 + c2, a2 - b + c2, a2 - b2 + c3)
        Triples.parChild(a + b2 + c2, a2 + b + c2, a2 + b2 + c3)
        Triples.parChild(-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3)

    @staticmethod
    def main():
        for i in range(2, 8):
            Triples.LIMIT = 10 ** i
            Triples.primCount = 0
            Triples.tripCount = 0
            Triples.parChild(Triples.THREE, Triples.FOUR, Triples.FIVE)
            print(f"{Triples.LIMIT}: {Triples.tripCount} triples, {Triples.primCount} primitive.")

Triples.main()