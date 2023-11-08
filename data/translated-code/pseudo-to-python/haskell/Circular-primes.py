def rotated(xs):
    if any(x < xs[0] for x in xs):
        return []
    else:
        rotatedList = rotate(xs)
        return list(map(asNum, take(len(xs) - 1, rotatedList)))

def rotate(xs):
    if not xs:
        return []
    else:
        firstElement = xs[0]
        restOfList = xs[1:]
        rotatedList = restOfList + [firstElement]
        return rotatedList + rotate(restOfList + [firstElement])

def asNum(n):
    if not n:
        return 0
    else:
        firstElement = n[0]
        restOfList = n[1:]
        if all(x == 1 for x in n):
            return int(''.join(map(str, n)))
        else:
            return (firstElement * (10 ** len(restOfList)) + asNum(restOfList))

def digits(n):
    if n == 0:
        return []
    else:
        d, r = divmod(n, 10)
        return digits(d) + [r]

def isCircular(repunit, n):
    if repunit:
        return millerRabinV(0, n)
    elif n < 10:
        return True
    elif n % 2 == 0:
        return False
    else:
        rotations = rotated(digits(n))
        if not rotations:
            return False
        elif any(x < n for x in rotations):
            return False
        else:
            return all(millerRabinV(0, x) for x in rotations)

def repunits():
    return go(2)

def go(n):
    return asNum([1]*n) + go(n + 1)

def asRepunit(n):
    return asNum([1]*n)

def main():
    print("The first 19 circular primes are:")
    print(circular(primes))
    print("The next 4 circular primes, in repunit format are:")
    for rep in reps(repunits):
        print("R(" + str(rep) + ")")
    print("The following repunits are probably circular primes:")
    for pair in checkReps:
        print("R(" + str(pair[0]) + ") : " + str(isCircular(True, asRepunit(pair[1]))) )