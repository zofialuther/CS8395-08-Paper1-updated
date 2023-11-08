```python
import math

class Floyd:
    def printTriangle(self, n):
        numsPrinted = 0
        for i in range(1, n+1):
            row = ""
            numOfCols = math.ceil(math.log10((i*(i-1))/2 + numsPrinted + 2))
            for j in range(1, i+1):
                row += str(j+numsPrinted).rjust(numOfCols, " ")
            print(row)
            numsPrinted += i
    
    def main(self):
        self.printTriangle(5)
        print()
        self.printTriangle(3)

Floyd().main()
```