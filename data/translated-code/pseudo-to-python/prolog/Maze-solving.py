```python
def maze_solve(Lig, Col):
    cell = []
    maze = []
    path = []
    for i in range(Lig+1):
        for j in range(Col+1):
            maze.append((i, j, []))
    # create window for maze
    # create entrance and exit
    # assert random cell
    # search for path
    # walk through the maze
    # display the path

def walk(Lig, Col):
    if path[0] == (Lig-1, Col-1):
        path.pop(0)
        path.append((Lig, Col))
    else:
        path.pop(0)
        # get the edges of the current maze cell
        # for each edge:
            # if the edge is not in the path:
                # assert new path with edge and current cell
                # walk(Lig, Col)

def display_path(_, path):
    if not path:
        pass
    else:
        # create a box at coordinates (C*30+60, L*30+60)
        # recursively display the remaining path

def search(D, Lig, Col, L, C):
    # generate random direction
    # find next cell in that direction
    # assert the new cell
    # update maze with new edges
    # erase line between current and new cell
    # recursively search with new cell

def erase_line(D, L, C, L1, C1):
    if C < C1:
        C2 = C1
    else:
        C2 = C
    # draw a white vertical line between (C2*30+50, L*30+51) and (C2*30+50, (L+1)*30+50)

def erase_line(D, L, C, L1, C):
    # draw a white horizontal line between (51+C*30, L*30+50) and (50+(C+1)*30, L*30+50)

def nextcell(Dir, Lig, Col, L, C, L1, C1):
    # try to move in the given direction
    # if not possible, try moving in other directions

def next(0, _Lig, _Col, L, C, L1, C):
    if L > 0 and (L-1, C) not in cell:
        L1 = L-1
        return True
    else:
        return False
    #(similarly for other directions)
```