from functools import reduce

def eApprox():
    return reduce(
        lambda a, x: a + 1 / x,
        scanl(mul)(1)(
            range(1, 18)
        ),
        0
    )

def main():
    print(eApprox())

def scanl(f):
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )

if __name__ == '__main__':
    main()