def main():
    printTriangle(5)
    printTriangle(14)

def printTriangle(n):
    print(str(n) + " rows:")
    rowNum = 1
    printMe = 1
    numsPrinted = 0
    while rowNum <= n:
        cols = math.ceil(math.log10(n*(n-1)/2 + numsPrinted + 2))
        print("%"+str(cols)+"d " % printMe, end="")
        if numsPrinted == rowNum:
            print()
            rowNum += 1
            numsPrinted = 0
        printMe += 1
        numsPrinted += 1