from Data.List import *
from Data.List.Ordered import *

def main():
    print(head([(x0, x1, x2, x3, x4) for x3 in range(1, 250) for x2 in range(1, x3) for x1 in range(1, x2) for x0 in range(1, x1) 
                 if ((x0 ** 5) + (x1 ** 5) + (x2 ** 5) + (x3 ** 5)) in [i ** 5 for i in range(1, x1)] 
                 for x4 in [elemIndex((x0 ** 5) + (x1 ** 5) + (x2 ** 5) + (x3 ** 5), [i ** 5 for i in range(1, x1)])]]))

main()