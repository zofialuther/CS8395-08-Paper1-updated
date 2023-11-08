def findBabbageNumber():
    return next((x for x in range(1, 1000000) if (x**2) % 1000000 == 269696))

def main():
    result = findBabbageNumber()
    print(f"{result} ^ 2 equals {result**2} !")

main()