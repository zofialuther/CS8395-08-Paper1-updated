from math import factorial

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
        a2 = 2 * a
        b2 = 2 * b
        c2 = 2 * c
        c3 = 3 * c
        Triples.parChild(a - b2 + c2, a2 - b + c2, a2 - b2 + c3)
        Triples.parChild(a + b2 + c2, a2 + b + c2, a2 + b2 + c3)
        Triples.parChild(-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3)

    @staticmethod
    def main():
        i = 100
        while i <= 10000000:
            Triples.LIMIT = i
            Triples.primCount = 0
            Triples.tripCount = 0
            Triples.parChild(3, 4, 5)
            print(str(Triples.LIMIT) + ": " + str(Triples.tripCount) + " triples, " + str(Triples.primCount) + " primitive.")
            i *= 10

Triples.main()