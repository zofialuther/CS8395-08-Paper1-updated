from Data.Char import digitToInt
from Data.Set import member, insert, empty

def isHappy(n):
    def p(s, n):
        if n == 1:
            return True
        if n in s:
            return False
        else:
            return p(insert(n, s), f(n))
    
    def f(n):
        return sum(map(lambda x: int(x)**2, str(n)))
    
    return p(empty, n)

def main():
    for i in range(1, 100):
        if isHappy(i):
            print(i)

main()