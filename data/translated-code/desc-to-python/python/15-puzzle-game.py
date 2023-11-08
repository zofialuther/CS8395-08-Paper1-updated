```python
import tkinter as tk
import random

class Board:
    def __init__(self):
        # Initialize game board with randomized game squares
        # Ensure solvability of the game
        pass

class Square:
    def __init__(self):
        # Represents individual squares on the game board
        pass

class Game:
    def __init__(self):
        # Set up game window
        # Handle creation of game board
        # Allow for interaction with game squares
        pass

    def process_move(self, square):
        # Process the move and check if the game has been won
        pass

class MainProgram:
    def __init__(self):
        # Create Tkinter window
        # Set title and dimensions
        # Initialize the game
        pass

    def play_game(self):
        # Allow for playing and restarting the game
        pass

# Create Tkinter window and run the game
root = tk.Tk()
root.title("15 Puzzle Game")
root.geometry("400x400")

game = MainProgram()
game.play_game()

root.mainloop()
```