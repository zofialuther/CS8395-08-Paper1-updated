```python
import math

class LawOfCosines:
    @staticmethod
    def main():
        LawOfCosines.generateTriples(13)
        LawOfCosines.generateTriples60(10000)
    
    @staticmethod
    def generateTriples(max):
        for coeff in [0, -1, 1]:
            count = 0
            print("Max side length %d, formula:  a*a + b*b %s= c*c" % (max, "" if coeff == 0 else ("-" if coeff < 0 else "+") + " a*b "))
            for a in range(1, max+1):
                for b in range(1, a+1):
                    val = a*a + b*b + coeff*a*b
                    c = int(math.sqrt(val) + .5)
                    if c > max:
                        break
                    if c*c == val:
                        print("  (%d, %d, %d)" % (a, b, c))
                        count += 1
            print("%d triangles" % count)

    @staticmethod
    def generateTriples60(max):
        count = 0
        print("\nExtra Credit.\nMax side length %d, sides different length, formula:  a*a + b*b - a*b = c*c" % max)
        for a in range(1, max+1):
            for b in range(1, a):
                val = a*a + b*b - a*b
                c = int(math.sqrt(val) + .5)
                if c*c == val:
                    count += 1
        print("%d triangles" % count)

LawOfCosines.main()
```