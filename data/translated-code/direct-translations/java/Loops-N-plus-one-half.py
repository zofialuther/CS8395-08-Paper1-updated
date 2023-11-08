def main():
    i = 1
    while True:
        print(i, end="")
        if i == 10:
            break
        print(", ", end="")
        i += 1
    print()

if __name__ == "__main__":
    main()