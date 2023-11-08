from fractions import Fraction

class Farey:
    @staticmethod
    def gen_farey(i):
        farey = set()
        for den in range(1, i + 1):
            for num in range(0, den + 1):
                farey.add(Fraction(num, den))
        return sorted(farey)

    @staticmethod
    def main():
        for i in range(1, 12):
            print("F" + str(i) + ": " + str(Farey.gen_farey(i)))

        for i in range(100, 1001, 100):
            print("F" + str(i) + ": " + str(len(Farey.gen_farey(i))) + " members")

Farey.main()