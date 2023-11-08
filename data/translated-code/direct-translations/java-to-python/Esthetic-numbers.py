import java.util.ArrayList
from typing import List

class EstheticNumbers:
    
    @staticmethod
    def isEsthetic(n: int, b: int) -> bool:
        if n == 0:
            return False
        i = n % b
        n2 = n // b
        while n2 > 0:
            j = n2 % b
            if abs(i - j) != 1:
                return False
            n2 //= b
            i = j
        return True

    @staticmethod
    def listEsths(n: int, n2: int, m: int, m2: int, perLine: int, all: bool) -> None:
        esths: List[int] = []
        
        def dfs(n: int, m: int, i: int) -> None:
            nonlocal esths
            if n <= i <= m:
                esths.append(i)
            if i == 0 or i > m:
                return
            d = i % 10
            i1 = i * 10 + d - 1
            i2 = i1 + 2
            if d == 0:
                dfs(n, m, i2)
            elif d == 9:
                dfs(n, m, i1)
            else:
                dfs(n, m, i1)
                dfs(n, m, i2)

        for i in range(10):
            dfs(n2, m2, i)

        le = len(esths)
        print(f"Base 10: {le} esthetic numbers between {n} and {m}:\n")
        if all:
            for i in range(len(esths)):
                print(f"{esths[i]} ", end='')
                if (i + 1) % perLine == 0:
                    print()
        else:
            for i in range(perLine):
                print(f"{esths[i]} ", end='')
            print()
            print("............")
            for i in range(le - perLine, le):
                print(f"{esths[i]} ", end='')
            print()
            print()

    @staticmethod
    def main():
        for b in range(2, 17):
            print(f"Base {b}: {4 * b}th to {6 * b}th esthetic numbers:\n")
            n = 1
            c = 0
            while c < 6 * b:
                if EstheticNumbers.isEsthetic(n, b):
                    c += 1
                    if c >= 4 * b:
                        print(f"{np.base_repr(n, b)} ", end='')
                n += 1
            print()

        print()
        
        # the following all use the obvious range limitations for the numbers in question
        EstheticNumbers.listEsths(1000, 1010, 9999, 9898, 16, True)
        EstheticNumbers.listEsths(int(1e8), 101010101, 13 * int(1e7), 123456789, 9, True)
        EstheticNumbers.listEsths(int(1e11), 101010101010, 13 * int(1e10), 123456789898, 7, False)
        EstheticNumbers.listEsths(int(1e14), 101010101010101, 13 * int(1e13), 123456789898989, 5, False)
        EstheticNumbers.listEsths(int(1e17), 101010101010101010, 13 * int(1e16), 123456789898989898, 4, False)