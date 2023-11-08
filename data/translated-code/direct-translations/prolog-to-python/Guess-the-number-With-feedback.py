print("Guess an integer between 1 and 10.")
guess = input("Guess the number: ")
if not guess.isdigit():
    print("Invalid input.")
else:
    guess = int(guess)
    if guess < 3:
        print("Your guess is too low.")