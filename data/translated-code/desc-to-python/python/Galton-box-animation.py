```python
class Ball:
    def __init__(self, position):
        self.position = position
    
    def update_position(self):
        # Update the position of the ball based on the simulation rules
        pass

class Board:
    def __init__(self, size):
        self.size = size
        self.balls = [Ball(0), Ball(2), Ball(4)]  # Example initial positions of the balls

    def print_board(self):
        # Print the current state of the board using ASCII art
        pass

def main():
    board = Board(5)  # Example board size
    while any(ball.position < board.size for ball in board.balls):
        for ball in board.balls:
            ball.update_position()
        board.print_board()

if __name__ == "__main__":
    main()
```