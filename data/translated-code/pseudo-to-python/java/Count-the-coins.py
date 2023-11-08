def countChanges(amount, coins):
    n = len(coins)
    cycle = 0
    for c in coins:
        if c <= amount and c >= cycle:
            cycle = c + 1
    cycle = cycle * n
    table = [0] * cycle
    for i in range(n):
        table[i] = 1
    for i in range(n, cycle):
        table[i] = 0
    pos = n
    for s in range(1, amount+1):
        for i in range(n):
            if i == 0 and pos >= cycle:
                pos = 0
            if coins[i] <= s:
                q = pos - (coins[i] * n)
                if q >= 0:
                    table[pos] = table[q]
                else:
                    table[pos] = table[q + cycle]
            if i != 0:
                table[pos] = table[pos] + table[pos - 1]
            pos = pos + 1
    return table[pos - 1]

coinsUsEu = [[100, 50, 25, 10, 5, 1], [200, 100, 50, 20, 10, 5, 2, 1]]
for coins in coinsUsEu:
    print(countChanges(100, coins[2:]))
    print(countChanges(100000, coins))
    print(countChanges(1000000, coins))
    print(countChanges(10000000, coins))