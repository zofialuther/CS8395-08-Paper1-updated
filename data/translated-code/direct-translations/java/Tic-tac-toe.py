```python
class TicTacToe:
    def __init__(self):
        self.marks = [[0, 0, 0, 0, 0, 0] for _ in range(8)]
        self.wins = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3],
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
            [7, 5, 3],
            [9, 5, 1]
        ]
        self.weights = [3, 2, 3, 2, 4, 2, 3, 2, 3]
        self.grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.knotcount = 3
        self.crosscount = 4
        self.totalcount = 5
        self.playerid = 0
        self.compid = 1
        self.truceid = 2
        self.playingid = 3
        self.movesPlayer = ""
        self.override = 0
        self.overridegrid = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        self.numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        self.crossbank = {}
        self.knotbank = {}

    def startMatch(self):
        print("Start?(y/n):", end='')
        choice = input()
        if choice == 'n' or choice == 'N':
            return
        print("Use a standard numpad as an entry grid, as so:\n")
        self.display(self.numpad)
        print("Begin")
        playerscore = 0
        compscore = 0
        while True:
            result = self.startGame()
            if result == self.playerid:
                playerscore += 1
            elif result == self.compid:
                compscore += 1
            print("Score: Player-" + str(playerscore) + " AI-" + str(compscore))
            print("Another?(y/n):", end='')
            choice = input()
            if choice == 'n' or choice == 'N':
                break
        print("Game over.")

    def put(self, cell, player):
        i = -1
        j = -1
        if cell == 1:
            i = 2
            j = 0
        # ... (similar cases for other cell values)

    def startGame(self):
        self.init()
        self.display(self.grid)
        status = self.playingid
        while status == self.playingid:
            self.put(self.playerMove(), 0)
            if self.override == 1:
                print("O wins.")
                return self.playerid
            status = self.checkForWin()
            if status != self.playingid:
                break
            self.put(self.compMove(), 1)
            status = self.checkForWin()
        return status
    
    # ... (other methods and class variables)

    def display(self, grid):
        for i in range(3):
            print("\n-------")
            print("|" + grid[i][0] + "|" + grid[i][1] + "|" + grid[i][2] + "|")
        print("-------")
```