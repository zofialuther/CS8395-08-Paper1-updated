def main():
    counter = 0
    number = 3
    while True:
        guess = int(input("Guess the number: "))
        if guess == number:
            print("Well guessed!")
            return True
        else:
            counter += 1
            if counter == 3:
                return False

main()