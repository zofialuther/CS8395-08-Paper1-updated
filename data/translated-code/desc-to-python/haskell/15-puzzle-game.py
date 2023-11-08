```python
# function to shuffle the puzzle
def shuffle_puzzle():
    # code for shuffling the puzzle

# function to apply moves
def apply_move(move):
    # code for applying the move to the puzzle

# function to check for valid moves
def check_valid_move(move):
    # code for checking if the move is valid

# function to print the current state of the puzzle
def print_puzzle():
    # code for printing the current state of the puzzle

# main function to prompt user for input and start game loop
def main():
    difficulty = input("Choose difficulty level: easy, medium, hard")
    # code for setting up the puzzle based on difficulty level
    shuffle_puzzle()
    print_puzzle()
    
    while not puzzle_solved:
        move = input("Enter your move: ")
        if check_valid_move(move):
            apply_move(move)
            print_puzzle()
        else:
            print("Invalid move. Try again.")
    
    print("Congratulations! You solved the puzzle.")

# start the game
main()
```