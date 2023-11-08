def properDivs(n):
    divs = []
    if n == 1:
        return divs
    divs.append(1)
    for x in range(2, n):
        if n % x == 0:
            divs.append(x)
    divs.sort()
    return divs

def main():
    for x in range(1, 11):
        print(str(x) + ": " + str(properDivs(x)))

    x = 0
    count = 0
    for n in range(1, 20001):
        if len(properDivs(n)) > count:
            x = n
            count = len(properDivs(n))
    print(str(x) + ": " + str(count))