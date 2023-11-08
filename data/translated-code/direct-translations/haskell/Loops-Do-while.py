def main():
    xs = [0]
    while (xs[0] <= 0) or (xs[0] % 6 != 0):
        xs = [xs[0] + 1] + xs
    for i in reversed(xs):
        print(i)

main()