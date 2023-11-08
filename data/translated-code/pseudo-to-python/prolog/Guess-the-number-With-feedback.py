def main():
    print("Guess an integer between 1 and 10")
    number = int(input("Enter your guess: "))
    while number < 1 or number > 10:
        print("Invalid input")
        number = int(input("Enter your guess: "))
    if number < 3:
        print("Your guess is too low")
    elif number > 3:
        print("Your guess is too high")
    else:
        print("Congratulations! You guessed it right!")

main()