def count(target, values):
    if target == 0:
        return 1
    elif target < 0 or not values:
        return 0
    else:
        return count(target - values[0], values) + count(target, values[1:])

def main():
    ways = count(100, [1, 5, 10, 25])
    print(ways)

main()