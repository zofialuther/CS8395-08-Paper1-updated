def binomialCoefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)

def faulhaberTriangle(p, n):
    triangle = []
    for i in range(1, n+1):
        row = []
        for j in range(i):
            coef = binomialCoefficient(i-1, j) * ((-1)**j)
            row.append(coef / (p+1))
        triangle.append(row)
    return triangle

def faulhaberSum(p, n):
    return n * (n+1) * (2*n+1) / (6 * (p+1))

def displayTriangle(triangle):
    for row in triangle:
        print(row)

def displayFaulhaberSum(p, n):
    print(f"The sum of the {p}-th powers of the first {n} positive integers is: {faulhaberSum(p, n)}")

# Test cases
triangle = faulhaberTriangle(2, 5)
displayTriangle(triangle)

displayFaulhaberSum(2, 5)