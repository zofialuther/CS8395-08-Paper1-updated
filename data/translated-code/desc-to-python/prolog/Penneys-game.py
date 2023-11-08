import random

def play_game():
    choices = ['heads', 'tails']
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (heads or tails): ")
    
    if player_choice not in choices:
        print("Invalid choice. Please enter heads or tails.")
        return
    
    print("Computer chose:", computer_choice)
    
    if computer_choice == player_choice:
        print("It's a tie!")
    elif (player_choice == 'heads' and computer_choice == 'tails') or (player_choice == 'tails' and computer_choice == 'heads'):
        print("You win!")
    else:
        print("Computer wins!")

play_game()