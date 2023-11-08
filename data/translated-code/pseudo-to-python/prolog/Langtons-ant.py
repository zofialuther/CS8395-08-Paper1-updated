def plot_point(Row, Col):
    # create a new 5x5 black box at position (Row, Col)
    pass

def update_win():
    # create a 500x500 window
    # find all the black points and plot them using plot_point function
    pass

def direction(Row, Col, direction):
    if direction == "left":
        if black(Row, Col) == True:
            retract_black(Row, Col)
    elif direction == "right":
        if black(Row, Col) == False:
            assert_black(Row, Col)

def move(direction, Row, Col):
    if Row < 0 or Col < 0 or Row > 99 or Col > 99:
        return
    if direction == "north":
        if direction(Row, Col, "left") == True:
            move("west", Row, Col-1)
        if direction(Row, Col, "right") == True:
            move("east", Row, Col+1)
    if direction == "south":
        if direction(Row, Col, "right") == True:
            move("west", Row, Col-1)
        if direction(Row, Col, "left") == True:
            move("east", Row, Col+1)
    if direction == "east":
        if direction(Row, Col, "right") == True:
            move("south", Row+1, Col)
        if direction(Row, Col, "left") == True:
            move("north", Row-1, Col)
    if direction == "west":
        if direction(Row, Col, "left") == True:
            move("south", Row+1, Col)
        if direction(Row, Col, "right") == True:
            move("north", Row-1, Col)

def go():
    # remove all black points
    # move north with starting position (49, 49)
    # call update_win function
    pass