from functools import reduce

def calculate_e(n):
    scanl_values = [1] + [1 / reduce(lambda x, y: x * y, range(1, i+1)) for i in range(1, n)]
    return reduce(lambda x, y: x + y, scanl_values)

def main():
    n = 10
    approx_e = calculate_e(n)
    print(f"Approximation for e with {n} iterations: {approx_e}")

main()