def divisors(n):
    result = []
    for i in range(1, n//2+1):
        if n % i == 0:
            result.append(i)
    return result

def main():
    range = list(range(1, 20001))
    divs = list(zip(range, map(sum, map(divisors, range)))
    pairs = []
    for n, nd in divs:
        for m, md in divs:
            if n < m and nd == m and md == n:
                pairs.append((n, m))
    print(pairs)