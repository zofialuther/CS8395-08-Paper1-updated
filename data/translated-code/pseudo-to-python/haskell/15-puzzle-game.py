```python
import array
import random

Puzzle = array.array

def main():
    print("Please enter the difficulty level: 0, 1 or 2")
    userInput = input()
    diffLevel = int(userInput)
    if userInput == "" or any(c < '0' or c > '9' for c in userInput) or diffLevel > 2 or diffLevel < 0:
        print("That is not a valid difficulty level.")
        main()
    else:
        shufflePuzzle([10, 50, 100][diffLevel], solvedPuzzle)
        gameLoop(puzzle)

def gameLoop(puzzle):
    if puzzle == solvedPuzzle:
        print("You solved the puzzle!")
        printPuzzle(puzzle)
    else:
        printPuzzle(puzzle)
        print("Please enter number to move")
        userInput = input()
        if any(c < '0' or c > '9' for c in userInput):
            print("That is not a valid number.")
            gameLoop(puzzle)
        else:
            move = int(userInput)
            if move not in validMoves(puzzle):
                print("This move is not available.")
                gameLoop(puzzle)
            else:
                gameLoop(applyMove(move, puzzle))

def validMoves(puzzle):
    rowEmpty, columnEmpty = findIndexOfNumber(16, puzzle)
    return [puzzle[row][column] for row in range(rowEmpty - 1, rowEmpty + 2) for column in range(columnEmpty - 1, columnEmpty + 2) if 4 > row >= 0 and 4 > column >= 0 and (row == rowEmpty) != (column == columnEmpty)]

def applyMove(numberToMove, puzzle):
    indexToMove = findIndexOfNumber(numberToMove, puzzle)
    emptyIndex = findIndexOfNumber(16, puzzle)
    puzzle[indexToMove] = 16
    puzzle[emptyIndex] = numberToMove
    return puzzle

def findIndexOfNumber(number, puzzle):
    indices = [(row, column) for row in range(4) for column in range(4) if puzzle[row][column] == number]
    if len(indices) == 1:
        return indices[0]
    else:
        raise Exception("BUG: number not in puzzle")

def printPuzzle(puzzle):
    print("+--+--+--+--+")
    for row in range(4):
        print(f"|{formatCell((row, 0))}|{formatCell((row, 1))}|{formatCell((row, 2))}|{formatCell((row, 3))}|")
        print("+--+--+--+--+")

def formatCell(idx):
    i = puzzle[idx]
    if i == 16:
        return "  "
    elif i > 9:
        return str(i)
    else:
        return " " + str(i)

solvedPuzzle = Puzzle('i', range(1, 17))

def shufflePuzzle(numOfShuffels, puzzle):
    if numOfShuffels == 0:
        return puzzle
    else:
        moves = validMoves(puzzle)
        randomIndex = random.randint(0, len(moves) - 1)
        move = moves[randomIndex]
        return shufflePuzzle(numOfShuffels - 1, applyMove(move, puzzle))
```