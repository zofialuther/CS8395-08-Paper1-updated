import math

def main():
    p5List = [i**5 for i in range(1, 1000)]
    
    for x3 in range(1, 250):
        for x2 in range(1, x3):
            for x1 in range(1, x2):
                for x0 in range(1, x1):
                    p5Sum = x0**5 + x1**5 + x2**5 + x3**5
                    if p5Sum in p5List:
                        x4 = p5List.index(p5Sum)
                        print((x0, x1, x2, x3, x4))
                        return

main()