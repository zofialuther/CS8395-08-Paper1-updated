def calcDigitalRoot(number, base):
    bi = int(number, base)
    additivePersistence = 0
    if bi < 0:
        bi = abs(bi)
    biBase = base
    while bi >= biBase:
        number = format(bi, 'x')
        bi = 0
        for i in range(len(number)):
            bi += int(number[i], base)
        additivePersistence += 1
    return [additivePersistence, bi]

def main(args):
    for arg in args:
        results = calcDigitalRoot(arg, 10)
        print(str(arg) + " has additive persistence " + str(results[0]) + " and digital root of " + str(results[1]))