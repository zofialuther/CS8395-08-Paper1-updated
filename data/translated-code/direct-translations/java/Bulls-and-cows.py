```python
import random

def has_dupes(num):
    digs = [False] * 10
    while num > 0:
        if digs[num % 10]:
            return True
        digs[num % 10] = True
        num //= 10
    return False

def main():
    gen = random.Random()
    target = 0
    while has_dupes(target := (gen.randint(1000, 9999))):
        pass
    target_str = str(target)
    guessed = False
    guesses = 0
    while not guessed:
        bulls = 0
        cows = 0
        guess = int(input("Guess a 4-digit number with no duplicate digits: "))
        if has_dupes(guess) or guess < 1000:
            continue
        guesses += 1
        guess_str = str(guess)
        for i in range(4):
            if guess_str[i] == target_str[i]:
                bulls += 1
            elif guess_str[i] in target_str:
                cows += 1
        if bulls == 4:
            guessed = True
        else:
            print(f"{cows} Cows and {bulls} Bulls.")
    print(f"You won after {guesses} guesses!")

if __name__ == "__main__":
    main()
```