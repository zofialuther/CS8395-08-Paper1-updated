import random

def generate_number():
    return random.sample(range(1, 10), 4)

def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def main():
    secret_number = generate_number()
    guessed = False

    while not guessed:
        user_guess = input("Enter your guess: ")
        user_guess = [int(x) for x in user_guess]
        bulls, cows = check_guess(secret_number, user_guess)
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            guessed = True
    print("Congratulations! You guessed the number!")

main()