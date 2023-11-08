def nthFib(n):
    def go(ab, _):
        return ab[1], ab[0]+ab[1]
    return reduce(go, range(1, n), (0, 1))[1]

if __name__ == '__main__':
    print('1000th term: ' + repr(nthFib(1000)))