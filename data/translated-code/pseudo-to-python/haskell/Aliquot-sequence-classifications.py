def divisors(n):
    return list(filter(lambda x: n % x == 0, range(1, n//2+1)))

class Class:
    def __init__(self):
        pass

def aliquot(n):
    if n == 0:
        return [0]
    else:
        return [n] + aliquot(sum(divisors(n)))

def classify(a):
    if a == []:
        return "Nonterminating"
    elif a == [0]:
        return "Terminating"
    elif len(a) == 1:
        return "Nonterminating"
    elif len(a) == 2:
        if a[0] == a[1]:
            return "Perfect"
        elif a[1] == 0:
            return "Terminating"
        else:
            return "Nonterminating"
    else:
        if a[0] == a[1]:
            return "Perfect"
        elif a[0] == a[2]:
            return "Amicable"
        elif a[0] in a[1:]:
            return "Sociable"
        else:
            d = classify(a[1:])
            if d == "Perfect":
                return "Aspiring"
            elif d == "Amicable" or d == "Sociable":
                return "Cyclic"
            else:
                return d

def main():
    for i in range(1,11):
        print(classify(aliquot(i)))
    for i in [11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488]:
        print(classify(aliquot(i)))