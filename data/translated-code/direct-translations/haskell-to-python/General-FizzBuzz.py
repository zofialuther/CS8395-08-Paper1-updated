def fizzEtc(rules):
    def nextLine(x, a):
        noise = ''.join([k for m, k in rules if x % m == 0])
        if not noise:
            return [str(x)] + a
        else:
            return [noise] + a
    return ["".join(x) for x in map(str, range(1, 21))]

def fizzTest():
    return fizzEtc([(3, "Fizz"), (5, "Buzz"), (7, "Baxx")])

def main():
    for line in fizzTest():
        print(line)

main()