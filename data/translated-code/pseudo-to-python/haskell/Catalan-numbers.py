cats1 = [math.prod(range(2, 2+n)) // math.prod(range(1, n+1)) for n in range(0, 20)]

cats2 = [1] + [sum([(cats2[i] * cats2[n-i-1]) for i in range(n)]) for n in range(1, 20)]

cats3 = list(itertools.accumulate([cats3[i] * 2 * (2 * (i+1) - 1) // (i + 2) for i in range(20)]))

def main():
    for l in [cats1, cats2, cats3]:
        print(l[:15])

main()