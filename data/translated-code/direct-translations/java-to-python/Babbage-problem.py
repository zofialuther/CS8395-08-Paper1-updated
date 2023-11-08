# Python equivalent of the given Java code

def main():
    # let n be zero
    n = 0

    # repeat the following action
    while True:
        # increase n by 1
        n += 1

        # while the modulo of n times n is not equal to 269696
        if n * n % 1000000 == 269696:
            break

    # show the result
    print(n)

# Call the main function
if __name__ == "__main__":
    main()