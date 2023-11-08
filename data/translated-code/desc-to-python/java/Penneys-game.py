```python
import random

def coin_toss():
    return random.choice(['heads', 'tails'])

def validate_input(choice, computer_choice):
    valid_choices = ['heads', 'tails']
    return choice in valid_choices and choice != computer_choice

def main():
    computer_choice = coin_toss()
    
    player_choice = input("Enter your choice (heads or tails): ")
    while not validate_input(player_choice, computer_choice):
        player_choice = input("Invalid choice. Enter your choice (heads or tails): ")
    
    sequence = ''
    while sequence != player_choice and sequence != computer_choice:
        sequence = coin_toss() + coin_toss() + coin_toss()
    
    if sequence == player_choice:
        print("Player wins!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()
```