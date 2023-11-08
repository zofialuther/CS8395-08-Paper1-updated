from inflect import engine

def spellOrdinal(n):
    return engine().ordinal(n)

numbers = [1, 2, 3, 4, 5, 11, 65, 100, 101, 272, 23456, 8007006005004003]

for n in numbers:
    print(str(n) + "\t" + spellOrdinal(n))