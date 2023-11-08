def arithmetic_geometric_mean(a, b, accuracy):
    x = (a + b) / 2
    y = (a * b) ** 0.5
    while abs(x - y) > accuracy:
        a = x
        b = y
        x = (a + b) / 2
        y = (a * b) ** 0.5
    return x

def relative_difference(a, b):
    return abs(a - b) / ((a + b) / 2)

def main():
    result = arithmetic_geometric_mean(1, 1 / (2 ** 0.5), 0.0001)
    print(result)

main()