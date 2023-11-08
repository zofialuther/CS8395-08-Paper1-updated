def divisors(n):
    return [x for x in range(1, n//2 + 1) if n % x == 0]

def classOf(n):
    if sum(divisors(n)) < n:
        return "deficient"
    elif sum(divisors(n)) == n:
        return "perfect"
    else:
        return "abundant"

def main():
    classes = [classOf(x) for x in range(1, 20001)]
    def printRes(w, c):
        count = len([x for x in classes if x == c])
        print(w + str(count))
    
    printRes("deficient: ", "deficient")
    printRes("perfect:   ", "perfect")
    printRes("abundant:  ", "abundant")

main()