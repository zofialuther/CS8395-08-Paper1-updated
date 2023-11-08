```
import random

def coin_toss_game():
    while True:
        user_choice = input("Pick heads or tails: ")
        cpu_choice = random.choice(["heads", "tails"])
        
        print("CPU chose:", cpu_choice)
        
        if user_choice == cpu_choice:
            print("You win!")
        else:
            print("CPU wins!")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

coin_toss_game()
```