def count(x, coins):
    if x == 0:
        return 1
    if not coins:
        return 0
    sum = 0
    for n in range(0, x // coins[0] + 1):
        sum += count(x - (n * coins[0]), coins[1:])
    return sum

def main():
    print(count(100, [1, 5, 10, 25]))