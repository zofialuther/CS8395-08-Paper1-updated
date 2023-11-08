def main():
    numbers = [1, 2, 3, 4, 5]
    numbers = list(map(lambda x: x+1, numbers))
    numbers.reverse()
    print(numbers)

if __name__ == "__main__":
    main()