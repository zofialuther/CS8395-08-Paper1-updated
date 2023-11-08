```python
import random

class Choice:
    Rock = 0
    Paper = 1
    Scissors = 2

def beats(player_choice, computer_choice):
    if (player_choice - computer_choice) % 3 == 1:
        return "Player wins"
    elif (player_choice - computer_choice) % 3 == 2:
        return "Computer wins"
    else:
        return "It's a tie"

def genrps():
    return random.choice([Choice.Rock, Choice.Paper, Choice.Scissors])

def getrps():
    choice = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    return choice

def game():
    player_score = 0
    computer_score = 0
    for _ in range(3):  # Play 3 rounds
        player_choice = getrps()
        computer_choice = genrps()
        outcome = beats(player_choice, computer_choice)
        print(outcome)
        if outcome == "Player wins":
            player_score += 1
        elif outcome == "Computer wins":
            computer_score += 1
    print("Final score - Player: {}, Computer: {}".format(player_score, computer_score))

def main():
    game()

if __name__ == "__main__":
    main()
```