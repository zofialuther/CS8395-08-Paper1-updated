def f(x):
    return 1/(x*x)

def main():
    start = 1
    end = 1000
    sum = 0

    for x in range(start, end+1):
        sum += f(x)

    print("Sum of f(x) from " + str(start) + " to " + str(end) + " is " + str(sum))

if __name__ == "__main__":
    main()