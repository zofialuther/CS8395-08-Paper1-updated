def prime(N):
    return N > 1 and all(N % i != 0 for i in range(2, int(N ** 0.5) + 1))

def primesByDiffs(primeList, diff, slides):
    if not primeList:
        return []
    else:
        return [slide for slide in slides if all(slide[i + 1] - slide[i] == diff[i] for i in range(len(diff)))]

def select(diffs, slide):
    if not diffs:
        return True
    else:
        return slide[1] - slide[0] == diffs[0] and select(diffs[1:], slide[1:])

def run(diffList, primeList):
    for diff in diffList:
        start = time.time()
        slideList = primesByDiffs(primeList, diff, [primeList])
        num = len(slideList)
        end = time.time()
        runtime = end - start
        print(f'number: {num} [time(ms) {runtime}] first: {slideList[0]}', end=' ')
        if slideList[1:]:
            print(f'last: {slideList[-1]}')
        else:
            print()

def do():
    num = 1000000
    start = time.time()
    primeList = [i for i in range(2, num + 1) if prime(i)]
    numPrimes = len(primeList)
    end = time.time()
    runtime = end - start
    print(f'there are {numPrimes} primes until {num} [time(ms) {runtime}]')
    diffList = [[1], [2], [2, 2], [2, 4], [4, 2], [2, 4, 6], [2, 6, 4], [4, 2, 6], [4, 6, 2], [6, 2, 4], [6, 4, 2]]
    run(diffList, primeList)