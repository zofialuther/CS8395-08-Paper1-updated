def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    return result

def classOf(n):
    sumOfDivisors = sum(divisors(n))
    if sumOfDivisors < n:
        return "deficient"
    elif sumOfDivisors == n:
        return "perfect"
    else:
        return "abundant"

def main():
    classes = []
    for i in range(1, 20001):
        classes.append(classOf(i))
    printRes("deficient: ", countOccurences("deficient", classes))
    printRes("perfect:   ", countOccurences("perfect", classes))
    printRes("abundant:  ", countOccurences("abundant", classes))

def printRes(string, count):
    print(string + str(count))

def countOccurences(val, arr):
    count = 0
    for element in arr:
        if element == val:
            count += 1
    return count