import tkinter
from tkinter import messagebox
import random

class Board:
    def __init__(self, playable):
        self.playable = playable
        # Other initialization code here

    # Other methods here

class Square:
    def __init__(self, row, column, text):
        self.row = row
        self.column = column
        self.text = text
        # Other initialization code here

    # Other methods here

class Game:
    def __init__(self, game_window):
        self.game_window = game_window
        # Other initialization code here

    def new_game(self):
        # Code to start a new game here

    def play_game(self):
        # Code to place squares on the board here

    def process_click(self):
        # Code to process when a square is clicked here

# Create an instance of the Tkinter window, set the title, size, and run the game
game_window = tkinter.Tk()
game_window.title("15 Puzzle")
game_window.geometry("400x400")

game = Game(game_window)
game.new_game()

game_window.mainloop()