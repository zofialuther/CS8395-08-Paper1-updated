def fizzEtc(rules):
    result = []
    x = 1
    while True:
        if not noise:
            result.append(x)
        else:
            result.append(''.join(noise))
        x += 1
        noise = []
        for rule in rules:
            if x % rule[0] == 0:
                noise += rule[1]
    return result

def fizzTest():
    return fizzEtc([(3, "Fizz"), (5, "Buzz"), (7, "Baxx")])

def main():
    testResult = fizzTest()
    for line in testResult[:20]:
        print(line)