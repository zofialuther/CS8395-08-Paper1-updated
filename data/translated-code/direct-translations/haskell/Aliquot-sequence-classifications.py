def divisors(n):
    return list(filter(lambda x: n % x == 0, range(1, n // 2 + 1)))

class Class(Enum):
    Terminating = 0
    Perfect = 1
    Amicable = 2
    Sociable = 3
    Aspiring = 4
    Cyclic = 5
    Nonterminating = 6

def aliquot(n):
    if n == 0:
        return [0]
    else:
        result = [n]
        while True:
            divs = divisors(n)
            n = sum(divs)
            if n in result:
                result.append(n)
                return result
            result.append(n)

def classify(arr):
    if len(arr) == 0:
        return Class.Nonterminating
    elif len(arr) == 1 and arr[0] == 0:
        return Class.Terminating
    elif len(arr) == 1:
        return Class.Nonterminating
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            return Class.Perfect
        elif arr[1] == 0:
            return Class.Terminating
        else:
            return Class.Nonterminating
    else:
        a, b, c = arr[:3]
        if a == b:
            return Class.Perfect
        elif a == c:
            return Class.Amicable
        elif a in arr[1:]:
            return Class.Sociable
        else:
            sub_class = classify(arr[1:])
            if sub_class == Class.Perfect:
                return Class.Aspiring
            elif sub_class == Class.Amicable or sub_class == Class.Sociable:
                return Class.Cyclic
            else:
                return sub_class

def main():
    for n in range(1, 11):
        result = classify(aliquot(n)[:16])
        print(result, aliquot(n)[:16])
    for n in [11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488]:
        result = classify(aliquot(n)[:16])
        print(result, aliquot(n)[:16])

if __name__ == "__main__":
    main()