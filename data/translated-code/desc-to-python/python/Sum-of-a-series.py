def seriesSumA(func, values):
    total = 0
    for value in values:
        total += func(value)
    return total

def seriesSumB(func, values):
    return sum(func(value) for value in values)

def main():
    values = list(range(1, 1001))
    series_sum_a = seriesSumA(lambda x: 1 / (x**2), values)
    series_sum_b = seriesSumB(lambda x: 1 / (x**2), values)
    print(f"Series sum using seriesSumA: {series_sum_a}")
    print(f"Series sum using seriesSumB: {series_sum_b}")

if __name__ == "__main__":
    main()