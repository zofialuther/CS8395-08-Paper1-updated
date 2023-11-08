import numpy as np
import random

def main():
    print("Please enter the difficulty level: 0, 1 or 2")
    userInput = input()
    diffLevel = int(userInput)
    if userInput == "" or any(c < '0' or c > '9' for c in userInput) or diffLevel > 2 or diffLevel < 0:
        print("That is not a valid difficulty level.")
        main()
    else:
        shufflePuzzle([10, 50, 100][diffLevel], solvedPuzzle)
        
def gameLoop(puzzle):
    if np.array_equal(puzzle, solvedPuzzle):
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
    moves = []
    for row in range(rowEmpty-1, rowEmpty+2):
        for column in range(columnEmpty-1, columnEmpty+2):
            if 0 <= row < 4 and 0 <= column < 4 and (row == rowEmpty) != (column == columnEmpty):
                moves.append(puzzle[row, column])
    return moves

def applyMove(numberToMove, puzzle):
    indexToMove = findIndexOfNumber(numberToMove, puzzle)
    emptyIndex = findIndexOfNumber(16, puzzle)
    new_puzzle = puzzle.copy()
    new_puzzle[indexToMove] = 16
    new_puzzle[emptyIndex] = numberToMove
    return new_puzzle

def findIndexOfNumber(number, puzzle):
    indices = np.array(np.where(puzzle == number))
    return tuple(indices.T[0])

def printPuzzle(puzzle):
    print("+--+--+--+--+")
    for i in range(4):
        row_string = "|"
        for j in range(4):
            row_string += formatCell((i, j)) + "|"
        print("+--+--+--+--+")
        print(row_string)
    print("+--+--+--+--+")

def formatCell(idx):
    i = puzzle[idx]
    if i == 16:
        return "  "
    elif i > 9:
        return str(i)
    else:
        return " " + str(i)

solvedPuzzle = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).reshape((4, 4))

def shufflePuzzle(numOfShuffles, puzzle):
    if numOfShuffles == 0:
        return puzzle
    else:
        moves = validMoves(puzzle)
        randomIndex = random.randint(0, len(moves) - 1)
        move = moves[randomIndex]
        return shufflePuzzle(numOfShuffles - 1, applyMove(move, puzzle))

if __name__ == "__main__":
    main()