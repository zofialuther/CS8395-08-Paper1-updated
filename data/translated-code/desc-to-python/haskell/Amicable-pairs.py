def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

def main():
    pairs = []
    for i in range(1, 20001):
        sum_divisors_i = sum(divisors(i))
        for j in range(i+1, 20001):
            if sum_divisors_i == sum(divisors(j)):
                pairs.append((i, j))
    print(pairs)

main()