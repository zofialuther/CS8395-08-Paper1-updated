def notDiag(q1, q2):
    return abs(q1[0] - q2[0]) != abs(q1[1] - q2[1])

def queens(board, n, result):
    if n == len(board):
        result.append(list(board))
        return
    for i in range(len(board)):
        board[n] = i
        if all(notDiag([n, board[n]], [j, board[j]]) for j in range(n)):
            queens(board, n+1, result)

def printBoard(board):
    for row in board:
        line = ""
        for i in range(len(board)):
            if i == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def main():
    board = [0] * 8
    result = []
    queens(board, 0, result)
    for r in result:
        printBoard(r)

if __name__ == "__main__":
    main()