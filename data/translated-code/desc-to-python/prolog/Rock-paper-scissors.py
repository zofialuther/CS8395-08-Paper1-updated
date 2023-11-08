import random

def play(previous_moves):
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    computer_choice = random.choice(previous_moves)
    result = beats(user_choice, computer_choice)
    print(f"The computer chose {computer_choice}. You {result}!")
    play(previous_moves + [user_choice])

def beats(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

play(["rock", "paper", "scissors"])