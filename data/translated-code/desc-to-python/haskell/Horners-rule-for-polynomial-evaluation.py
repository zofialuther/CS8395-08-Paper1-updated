def horner(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]
    return result

def main():
    result = horner(3, [-19, 7, -4, 6])
    print(result)

main()