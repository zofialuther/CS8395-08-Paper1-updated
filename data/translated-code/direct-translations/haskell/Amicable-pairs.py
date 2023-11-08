def divisors(n):
    return list(filter(lambda x: n % x == 0, range(1, n // 2 + 1)))

def main():
    range_ = list(range(1, 20001))
    divs = [(n, sum(divisors(n))) for n in range_]
    pairs = [(n, m) for (n, nd) in divs for (m, md) in divs if n < m and nd == m and md == n]
    print(pairs)

main()