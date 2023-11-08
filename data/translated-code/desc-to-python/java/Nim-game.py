```python
# Python code for simulating a game of Nim
tokens = 10

while tokens > 0:
    player_move = int(input("Enter your move (1-3): "))
    if player_move < 1 or player_move > 3:
        print("Invalid move. Please enter a number between 1 and 3.")
        continue
    tokens -= player_move
    if tokens <= 0:
        print("You win!")
        break
    computer_move = 4 - player_move
    print("Computer removes", computer_move, "tokens.")
    tokens -= computer_move
    if tokens <= 0:
        print("Computer wins!")
        break
```