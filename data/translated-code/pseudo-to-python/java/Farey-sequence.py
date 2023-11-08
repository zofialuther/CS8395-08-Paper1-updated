from fractions import Fraction

def genFarey(i):
    farey = set()
    for den in range(1, i+1):
        for num in range(0, den+1):
            farey.add(Fraction(num, den))
    return sorted(farey)

for i in range(1, 12):
    print("F" + str(i) + ": " + str(genFarey(i)))

for i in range(100, 1100, 100):
    print("F" + str(i) + ": " + str(len(genFarey(i))) + " members")