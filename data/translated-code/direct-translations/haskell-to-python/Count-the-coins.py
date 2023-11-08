def count(x, coins):
    if x == 0:
        return 1
    if not coins:
        return 0
    c = coins[0]
    rest = coins[1:]
    return sum(count(x - n * c, rest) for n in range(x // c + 1))

def main():
    print(count(100, [1, 5, 10, 25]))

if __name__ == "__main__":
    main()