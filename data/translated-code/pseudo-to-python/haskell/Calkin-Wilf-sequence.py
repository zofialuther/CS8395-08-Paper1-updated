def calkinWilfs():
    return iterate(lambda x: recip(succ(((2 * x) - floor(2 * x)))), 1)

def calkinWilfIdx(rational):
    return rld(cfo(rational))

def cfo(rational):
    return oddLen(cf(rational))

def cf(rational):
    return unfoldr(lambda r: (succ(n), Nothing) if properFraction(r) == (n, 1) else (n, Nothing) if properFraction(r) == (n, 0) else (n, Just(recip(f))))

def oddLen(nonEmptyInt):
    return fromList(go(toList(nonEmptyInt)))

    def go(list):
        return [x, pred(y), 1] if list == [x, y] else x:y:go(zs) if len(list) > 2 else xs

def rld(nonEmptyInt):
    return snd(foldr(lambda i, b_n: (not b, (n * (2 ** i)) + 0) if b == True else (not b, (n * (2 ** i)) + (2 ** i - 1)), True, 0))

def main():
    forM_(take(20, zip(range(1, 21), calkinWilfs())), lambda i, r: printf("%2d  %s\n", i, show(r)))
    r = 83116 / 51639
    printf("\n%s is at index %d of the Calkin-Wilf sequence.\n", show(r), calkinWilfIdx(r))