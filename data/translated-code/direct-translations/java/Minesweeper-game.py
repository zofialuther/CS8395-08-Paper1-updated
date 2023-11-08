```python
import random
import tkinter as tk
from tkinter import messagebox

class Cell:
    def __init__(self):
        self.isMine = False
        self.isFlagged = False
        self.isCovered = True
        self.number = 0

    def flag(self):
        self.isFlagged = True

    def unflag(self):
        self.isFlagged = False

    def setMine(self):
        self.isMine = True

    def reveal(self):
        self.isCovered = False

    def setNumber(self, i):
        self.number = i

    def getNumber(self):
        return self.number

    def isFlagged(self):
        return self.isFlagged

    def isCovered(self):
        return self.isCovered

class Board(tk.Canvas):
    def __init__(self, master, mine):
        super().__init__(master, width=mine.getx() * 20, height=mine.gety() * 20)
        self.mine = mine
        self.cells = self.mine.getCells()
        self.bind("<Button-1>", self.on_left_click)
        self.bind("<Button-3>", self.on_right_click)
        self.draw_board()

    def draw_board(self):
        for i in range(self.mine.getx()):
            for j in range(self.mine.gety()):
                current = self.cells[i][j]

                if current.isFlagged():
                    if current.isMine and self.mine.isFinished():
                        self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="orange")
                    elif self.mine.isFinished():
                        self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="yellow")
                    else:
                        self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="green")
                elif current.isCovered():
                    self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="dark gray")
                elif current.isMine:
                    self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="red")
                else:
                    self.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill="light gray")

                if not current.isCovered():
                    number = current.getNumber()
                    if number > 0:
                        self.create_text(i * 20 + 10, j * 20 + 10, text=str(number))

    def on_left_click(self, event):
        x = event.x // 20
        y = event.y // 20
        self.mine.select(x, y)
        self.draw_board()

    def on_right_click(self, event):
        x = event.x // 20
        y = event.y // 20
        self.mine.mark(x, y)
        self.draw_board()

class Minesweeper:
    def __init__(self, x, y, d):
        self.width = x
        self.height = y
        self.difficulty = d
        self.cells = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        self.finished = False
        self.reset()

        self.window = tk.Tk()
        self.window.title("Minesweeper")
        self.window.resizable(False, False)

        self.board = Board(self.window, self)
        self.board.pack()

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.window.mainloop()

    def select(self, x, y):
        if self.cells[x][y].isFlagged:
            return

        self.cells[x][y].reveal()
        self.reset_marks()
        self.board.draw_board()

        if self.cells[x][y].isMine:
            self.lose()
        elif self.won():
            self.win()

    def set_numbers(self):
        # Implementation of set_numbers method

    def mark(self, x, y):
        if self.cells[x][y].isFlagged:
            self.cells[x][y].unflag()
        elif self.cells[x][y].isCovered:
            self.cells[x][y].flag()

        self.reset_marks()

    def reset_marks(self):
        for i in range(self.width):
            for j in range(self.height):
                if not self.cells[i][j].isCovered:
                    self.cells[i][j].unflag()

    def reset(self):
        random.seed()
        self.finished = False

        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j] = Cell()
                if random.randint(0, 100) < self.difficulty:
                    self.cells[i][j].setMine()

        self.set_numbers()
        self.board.draw_board()

    def getx(self):
        return self.width

    def gety(self):
        return self.height

    def getCells(self):
        return self.cells

    def refresh(self):
        self.board.draw_board()

    def win(self):
        self.finished = True
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].reveal()
                if not self.cells[i][j].isMine:
                    self.cells[i][j].unflag()

        self.refresh()
        messagebox.showinfo("Congratulations", "You won!")
        self.reset()

    def lose(self):
        self.finished = True
        for i in range(self.width):
            for j in range(self.height):
                if not self.cells[i][j].isCovered:
                    self.cells[i][j].unflag()
                self.cells[i][j].reveal()

        self.refresh()
        messagebox.showinfo("Game Over", "GAME OVER.")
        self.reset()

    def won(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[i][j].isCovered and not self.cells[i][j].isMine:
                    return False
        return True

    def isFinished(self):
        return self.finished

if __name__ == "__main__":
    x = intErrorTrap(0, 60)
    y = intErrorTrap(0, 30)
    d = intErrorTrap(0, 100)
    Minesweeper(x, y, d)
```