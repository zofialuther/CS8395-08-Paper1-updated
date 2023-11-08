from itertools import accumulate

def eth_mult(n, m):
    def half(num):
        return (num // 2, num % 2) if num != 0 else (0, 0)

    def added_where_odd(pair, result):
        return result + pair[1] if pair[0] != 0 else result

    halves = accumulate([n], lambda acc, _: half(acc))
    result = list(zip(halves, accumulate([m], lambda acc, _: acc + m)))
    return sum(added_where_odd(pair, result) for pair in result)

def main():
    print(eth_mult(17, 34))
    print(eth_mult(3, 34))
    print(eth_mult(17, "34"))
    print(eth_mult(17, [3, 4]))

if __name__ == "__main__":
    main()