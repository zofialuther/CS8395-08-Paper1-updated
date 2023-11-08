# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate the binomial coefficient
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

# Function to generate the first 5 rows of Pascal's triangle
def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [binomial_coefficient(i, j) for j in range(i+1)]
        triangle.append(row)
    return triangle

# Display the first 5 rows of Pascal's triangle
print(generate_pascals_triangle(5))