from collections import namedtuple

class Lychrel:

    cache = {}

    Tuple = namedtuple('Tuple', ['flag', 'bi'])

    @staticmethod
    def rev(bi):
        s = str(bi)[::-1]
        return int(s)

    @staticmethod
    def lychrel(n):
        if n in Lychrel.cache:
            return Lychrel.cache[n]

        r = Lychrel.rev(n)
        res = Lychrel.Tuple(True, n)
        seen = []

        for i in range(500):
            n += r
            r = Lychrel.rev(n)

            if n == r:
                res = Lychrel.Tuple(False, 0)
                break

            if n in Lychrel.cache:
                res = Lychrel.cache[n]
                break

            seen.append(n)

        for bi in seen:
            Lychrel.cache[bi] = res

        return res

    @staticmethod
    def main():
        seeds = []
        related = []
        palin = []

        for i in range(1, 10001):
            n = i

            t = Lychrel.lychrel(n)

            if not t.flag:
                continue

            if n == t.bi:
                seeds.append(t.bi)
            else:
                related.append(t.bi)

            if n == t.bi:
                palin.append(t.bi)

        print(f"{len(seeds)} Lychrel seeds: {seeds}")
        print(f"{len(related)} Lychrel related")
        print(f"{len(palin)} Lychrel palindromes: {palin}")

Lychrel.main()