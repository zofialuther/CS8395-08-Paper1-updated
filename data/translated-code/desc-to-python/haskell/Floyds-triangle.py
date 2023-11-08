def floyd(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=' ')
            num += 1
        print()

def floyds():
    n = 1
    while True:
        yield floyd(n)
        n += 1

def main():
    # Print the first 5 levels of Floyd's Triangle
    for level in floyds():
        if level > 5:
            break
        print(level)
    
    # Print the first 14 levels of Floyd's Triangle
    for level in floyds():
        if level > 14:
            break
        print(level)