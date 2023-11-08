def initialize_minesweeper_game(width, height):
    print("Welcome to Minesweeper!")
    print("Instructions: ...")

def create_new_grid():
    flat_list_of_cells = []
    # Generate flat list of cells
    # Calculate number of bombs
    # Add bombs to the grid list
    # Randomize the grid list and convert to 2D array
    # Populate hidden part of the grid with number of bombs next to each cell

def play_game():
    while not win_condition:
        if lose_condition:
            print("You lose!")
            break
        else:
            user_input = get_user_input()
            perform_operation(user_input)

def get_value_from_grid(x, y):
    # Get value from the grid by X Y

def set_value_on_grid(x, y, value):
    # Set value on the grid by X Y

def number_of_bombs_next_to_cell(x, y):
    # Determine number of bombs next to a cell

def print_grid():
    # Print the grid

def is_game_still_playing():
    # Determine if the game is still being played

def has_game_been_won():
    # Determine if the game has been won

def get_user_operation_from_input(user_input):
    # Parse the user input to determine the operation and cell coordinates

def perform_operation(user_input):
    if operation == "mark_as_bomb":
        mark_cell_as_bomb(x, y)
    elif operation == "open_cell":
        open_cell(x, y)
    elif operation == "expose_grid":
        expose_grid()
        
def mark_cell_as_bomb(x, y):
    # Mark a cell as containing a bomb

def open_cell(x, y):
    # Open a cell, revealing if it contains a bomb or a number

def expose_grid():
    # Expose the grid by checking adjacent cells and updating the grid accordingly
```