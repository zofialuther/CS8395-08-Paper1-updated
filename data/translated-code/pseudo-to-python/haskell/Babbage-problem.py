def findBabbageNumber():
    return next(x for x in range(1, 1000000) if (x**2) % 1000000 == 269696)

def main():
    babbage_num = findBabbageNumber()
    print(f"{babbage_num} ^ 2 equals {babbage_num**2}!")