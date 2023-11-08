from array import array
from math import factorial

class CountTheCoins:
    @staticmethod
    def count_changes(amount, coins):
        n = len(coins)
        cycle = 0
        for c in coins:
            if c <= amount and c >= cycle:
                cycle = c + 1
        cycle *= n
        table = array('q', [0] * cycle)
        table[:n] = [1] * n

        pos = n
        for s in range(1, amount + 1):
            for i in range(n):
                if i == 0 and pos >= cycle:
                    pos = 0
                if coins[i] <= s:
                    q = pos - (coins[i] * n)
                    table[pos] = table[q] if q >= 0 else table[q + cycle]
                if i != 0:
                    table[pos] += table[pos - 1]
                pos += 1

        return table[pos - 1]

    @staticmethod
    def main():
        coins_us_eu = [[100, 50, 25, 10, 5, 1],
                       [200, 100, 50, 20, 10, 5, 2, 1]]

        for coins in coins_us_eu:
            print(CountTheCoins.count_changes(100, coins[2:]))
            print(CountTheCoins.count_changes(100000, coins))
            print(CountTheCoins.count_changes(1000000, coins))
            print(CountTheCoins.count_changes(10000000, coins), "\n")
            
if __name__ == "__main__":
    CountTheCoins.main()