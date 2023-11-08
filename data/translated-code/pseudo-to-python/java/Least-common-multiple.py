from math import gcd

class LCM:
    def main():
        aScanner = input("Enter the value of m:")
        m = int(aScanner)
        aScanner = input("Enter the value of n:")
        n = int(aScanner)
        lcm = (n if n == m or n == 1 else (m if m == 1 else 0))
        if lcm == 0:
            mm = m
            nn = n
            while mm != nn:
                while mm < nn:
                    mm += m
                while nn < mm:
                    nn += n
            lcm = mm
        print("lcm(" + str(m) + ", " + str(n) + ") = " + str(lcm))

LCM.main()