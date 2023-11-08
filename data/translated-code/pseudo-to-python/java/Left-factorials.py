def factorial(n):
    ans = 1
    for x in range(1, n+1):
        ans = ans * x
    return ans

def leftFact(n):
    ans = 0
    for k in range(0, n):
        ans = ans + factorial(k)
    return ans

def main():
    for i in range(0, 11):
        print("!" + str(i) + " = " + str(leftFact(i)))

    for i in range(20, 111, 10):
        print("!" + str(i) + " = " + str(leftFact(i)))

    for i in range(1000, 10001, 1000):
        print("!" + str(i) + " has " + str(len(str(leftFact(i)))) + " digits")