```python
def StartMatch():
    br = input
    print("Start?(y/n):")
    choice = 'y'
    try:
        choice = br.readLine().charAt(0)
    except Exception as e:
        print(e.getMessage())
    
    if choice == 'n' OR choice == 'N':
        return
    
    print("Use a standard numpad as an entry grid, as so:\n")
    display(numpad)
    print("Begin")
    playerscore = 0
    compscore = 0
    while True:
        result = startGame()
        if result == playerid:
            playerscore += 1
        elif result == compid:
            compscore += 1
        print("Score: Player-" + str(playerscore) + " AI-" + str(compscore))
        print("Another?(y/n):")
        try:
            choice = br.readLine().charAt(0)
        except Exception as e:
            print(e.getMessage())
        if choice == 'n' OR choice == 'N':
            break
    
    print("Game over.")

def StartGame():
    init()
    display(grid)
    status = playingid
    while status == playingid:
        put(playerMove(), 0)
        if override == 1:
            print("O wins.")
            return playerid
        status = checkForWin()
        if status != playingid:
            break
        try:
            Thread.sleep(1000)
        except Exception as e:
            print(e.getMessage())
        put(compMove(), 1)
        status = checkForWin()
    return status

def Init():
    movesPlayer = ""
    override = 0
    marks = [[0 for x in range(6)] for y in range(8)]
    wins = [[7,8,9],
            [4,5,6],
            [1,2,3],
            [7,4,1],
            [8,5,2],
            [9,6,3],
            [7,5,3],
            [9,5,1]]
    weights = [3,2,3,2,4,2,3,2,3]
    grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    crossbank = {}
    knotbank = {}

def put(cell, player):
    i = -1
    j = -1
    if cell == 1:
        i = 2
        j = 0
    elif cell == 2:
        i = 2
        j = 1
    elif cell == 3:
        i = 2
        j = 2
    #... (other cases)
    else:
        display(overridegrid)
        return
    mark = 'x'
    if player == 0:
        mark = 'o'
    grid[i][j] = mark
    display(grid)

def playerMove():
    print("What's your move?: ")
    br = input
    cell = 0
    okay = 0
    while okay == 0:
        try:
            cell = int(br.readLine())
        except Exception as e:
            print(e.getMessage())
        if cell == 7494:
            override = 1
            return -1
        #... (other conditions)
        else:
            okay = 1
    playerMoved(cell)
    return cell

def playerMoved(cell):
    movesPlayer += cell
    mark(cell, 0)
    fixWeights()
    knotbank.put(cell, 0)

def checkForWin():
    crossflag = 0
    knotflag = 0
    for i in range(len(wins)):
        #... (other conditions)
    if knotflag == 1:
        display(grid)
        print("O wins.")
        return playerid
    #... (other conditions)
    return truceid

def display(grid):
    for i in range(3):
        print("\n-------")
        print("|")
        for j in range(2):
            print(grid[i][j] + "|")
    print("\n-------")
```