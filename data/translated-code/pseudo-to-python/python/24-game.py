```python
import random
import re

chars = ["(", ")", "/", "+", "-", "*"]

while True:
    charsandints = []
    ints = []
    
    for i in range(4):
        ints.append(str(random.randint(1, 10)))
    
    charsandints = chars + ints
    print("Numbers are:", " ".join(ints))
    guess = input("Enter your guess: ")
    
    if guess == "q":
        break
    elif guess == "|":
        pass
    else:
        flag = True
        for char in guess:
            if char not in charsandints or guess.count(char) > charsandints.count(char):
                flag = False
        if re.search(r'\d{2}', guess):
            print("You cannot combine digits")
            break
        if flag:
            print("Your result is:", eval(guess))
            if eval(guess) == 24:
                print("You won")
                break
            else:
                print("You lost")
                break
        else:
            print("You cannot use anything other than", " ".join(charsandints))
            break

print("Thanks for playing")
```