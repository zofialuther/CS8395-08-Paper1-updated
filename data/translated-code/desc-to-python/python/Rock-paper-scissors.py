import random

choices = ['rock', 'paper', 'scissors']
rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors) or type 'quit' to exit: ")
    
    if user_choice.lower() in ['quit', 'exit']:
        break
    
    if user_choice.lower() not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    if computer_choice == user_choice.lower():
        print("It's a tie!")
    elif rules[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer wins!")
    
print("Thanks for playing!")