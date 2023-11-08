```python
import tkinter as tk

def plot_point(row, col):
    c = tk.Canvas(window, width=5, height=5)
    x = col * 5 - 2
    y = row * 5 - 2
    c.create_rectangle(0, 0, 5, 5, fill="blue")
    c.create_rectangle(x, y, x+5, y+5, fill="black")
    c.pack()

def update_win():
    global window
    window = tk.Tk()
    window.title('Langtons Ant')
    window.geometry('500x500')
    for point in black_points:
        plot_point(point[0], point[1])
    window.mainloop()

def direction(row, col, dir):
    if (row, col) in black_points:
        black_points.remove((row, col))
    else:
        black_points.append((row, col))

def move(dir, row, col):
    if row < 0 or col < 0 or row > 99 or col > 99:
        return
    if dir == 'north':
        if (row, col) in black_points:
            direction(row, col, 'left')
            col -= 1
            move('west', row, col)
        else:
            direction(row, col, 'right')
            col += 1
            move('east', row, col)
    elif dir == 'south':
        if (row, col) in black_points:
            direction(row, col, 'right')
            col -= 1
            move('west', row, col)
        else:
            direction(row, col, 'left')
            col += 1
            move('east', row, col)
    elif dir == 'east':
        if (row, col) in black_points:
            direction(row, col, 'right')
            row += 1
            move('south', row, col)
        else:
            direction(row, col, 'left')
            row -= 1
            move('north', row, col)
    elif dir == 'west':
        if (row, col) in black_points:
            direction(row, col, 'left')
            row += 1
            move('south', row, col)
        else:
            direction(row, col, 'right')
            row -= 1
            move('north', row, col)

def go():
    global black_points
    black_points = []
    move('north', 49, 49)
    update_win()

go()
```