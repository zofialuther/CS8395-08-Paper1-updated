```
def play_game():
    dots = 20
    while dots > 0:
        player_turn = int(input("How many dots do you want to take? "))
        while player_turn < 1 or player_turn > 3 or player_turn > dots:
            player_turn = int(input("Invalid input. Please choose 1, 2, or 3 dots: "))
        dots -= player_turn
        if dots <= 0:
            print("You win!")
            break
        computer_turn = 3 - player_turn
        print("The computer takes", computer_turn, "dots.")
        dots -= computer_turn
        if dots <= 0:
            print("The computer wins!")
            break
```