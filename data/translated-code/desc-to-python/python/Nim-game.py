```python
tokens = 10

while tokens > 0:
    player_move = int(input("How many tokens would you like to take? "))
    tokens -= player_move
    if tokens <= 0:
        print("Computer wins!")
        break
    computer_move = 1  # Replace with logic for computer's move
    tokens -= computer_move
    if tokens <= 0:
        print("Player wins!")
        break
```