import sys
import os
import random
import time

def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def update(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        
    def fall(self):
        self.y -= 1

class Board:
    def __init__(self, width, well_depth, N, shift):
        self.balls = []
        self.fallen = []
        self.width = width
        self.well_depth = well_depth
        self.N = N
        self.shift = shift
        
    def update(self):
        for ball in self.balls:
            ball.update()
            if ball.y < self.well_depth:
                self.fallen.append(ball)
                self.balls.remove(ball)
        
    def count_balls(self):
        return len(self.balls)
    
    def add_ball(self, ball):
        self.balls.append(ball)
    
    def print_board(self):
        # code to print the board
        
    def print_specific_ball(self, ball):
        # code to print a specific ball
        
    def print_all_balls(self):
        # code to print all the balls on the board

def main():
    board = Board(10, 5, 3, 2)
    ball = Ball()
    board.add_ball(ball)
    while board.count_balls() > 0:
        board.print_board()
        board.update()
        board.print_board()
        board.update()
        new_ball = Ball()
        board.add_ball(new_ball)

if __name__ == "__main__":
    main()