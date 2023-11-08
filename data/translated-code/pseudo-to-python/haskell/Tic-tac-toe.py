```python
import random
import string
from typing import List, Tuple, Union

def tictactoe(a: str) -> bool:
    return tictactoeFor('X', a) != tictactoeFor('O', a)

def tictactoeFor(n: str, s: str) -> bool:
    return [n, n, n] in [[s[0], s[1], s[2]], [s[3], s[4], s[5]], [s[6], s[7], s[8]], [s[0], s[3], s[6]], [s[1], s[4], s[7]], [s[2], s[5], s[8]], [s[0], s[4], s[8]], [s[2], s[4], s[6]]]

def start() -> str:
    return "         "

def isPossible(n: int, game: str) -> bool:
    return game[n] not in "XO"

def place(i: int, c: str, game: str) -> Union[str, str]:
    if isPossible(i, game):
        return game[:i] + c + game[i+1:]
    else:
        return game

def developGame(iterateMore: bool, moves: int, i: int, player: str, game: str) -> Tuple[int, str, str]:
    if i > 8:
        if iterateMore:
            return developGame(False, moves, 0, player, game)
        else:
            return moves, player, game
    elif moves == 9 or tictactoeFor(player, game):
        return moves, player, game
    else:
        otherPlayer = changePlayer(player)
        result = place(i, otherPlayer, game)
        if isinstance(result, str):
            return developGame(iterateMore, moves, (i + 1), otherPlayer, game)
        else:
            newGame = result
            return developGame(iterateMore, (moves + 1), 0, otherPlayer, newGame)

def bestMoveFor(player: str, game: str) -> int:
    continuations = [(x, developGame(True, 0, x, player, game)) for x in range(9)]
    move = lambda x: x[1][0]
    bestMove, _ = min(continuations, key=lambda x: x[1][0])
    return bestMove

def canBlock(p: str, s: str) -> Union[int, None]:
    def blockable(xs):
        if xs.count(otherPlayer) == 2:
            x = next((i for i, x in enumerate(xs) if x in "123456789"), None)
            if x is not None:
                return int(x)
        return None
    otherPlayer = changePlayer(p)
    return next(filter(None, map(blockable, [[s[0], s[1], s[2]], [s[3], s[4], s[5]], [s[6], s[7], s[8]], [s[0], s[3], s[6]], [s[1], s[4], s[7]], [s[2], s[5], s[8]], [s[0], s[4], s[8]], [s[2], s[4], s[6]]]), None)

def showGame(s: str) -> str:
    topBottom = "+----+---+---+---+\n"
    row = lambda n, x: "| " + n + "+ | " + " | ".join(x) + " |\n" + topBottom
    return topBottom + "|    | 1 | 2 | 3 |\n" + topBottom + row("0", [s[0], s[1], s[2]]) + row("3", [s[3], s[4], s[5]]) + row("6", [s[6], s[7], s[8]])

def enterNumber() -> int:
    c = input("Enter a number: ")
    if c in "123456789":
        print("")
        return int(c)
    else:
        print("\nPlease enter a digit!")
        return enterNumber()

def turn(count: int, player: str, game: str) -> Tuple[int, str, str]:
    print("Please tell me where you want to put an " + player + ": ")
    pos = enterNumber()
    result = place(pos - 1, player, game)
    if isinstance(result, str):
        return count + 1, changePlayer(player), result
    else:
        oldGame = result
        print("That place is already taken!\n")
        return turn(count, player, oldGame)

def changePlayer(player: str) -> str:
    if player == 'O':
        return 'X'
    elif player == 'X':
        return 'O'

def autoTurn(forceRandom: bool, count: int, player: str, game: str) -> Tuple[int, str, str]:
    i = random.randint(0, 8) if count == 0 or forceRandom else canBlock(player, game)
    result = place(i, player, game)
    if isinstance(result, str):
        return autoTurn(True, count, player, result)
    else:
        newGame = result
        print("It's player " + player + "'s turn.")
        return count + 1, changePlayer(player), newGame

def play(auto: int, cpg: Tuple[int, str, str]) -> None:
    newcpg = cpg
    if auto == 0:
        newcpg = turn(*cpg)
    elif auto == 1:
        newcpg = autoTurn(False, *cpg)
    elif auto == 2:
        if cpg[1] == 'X':
            newcpg = autoTurn(False, *cpg)
        else:
            newcpg = turn(*cpg)
    elif auto == 3:
        if cpg[1] == 'O':
            newcpg = autoTurn(False, *cpg)
        else:
            newcpg = turn(*cpg)
    print("\n" + showGame(newcpg[2]))
    if tictactoe(newcpg[2]):
        print("Player " + changePlayer(newcpg[1]) + " wins!\n")
    elif newcpg[0] == 9:
        print("Draw!\n")
    else:
        play(auto, newcpg)

def main() -> None:
    a = input().split()
    if not a:
        usage()
    else:
        option = a[0]
        if option in ["0", "1", "2", "3"]:
            print("\n" + showGame(start()))
            m = int(option)
            play(m, (0, 'X', start()))
        else:
            usage()

def usage() -> None:
    print("TIC-TAC-TOE GAME\n================\n")
    print("How do you want to play?")
    print("Run the program with one of the following options.")
    print("0 : both players are human")
    print("1 : both players are computer")
    print("2 : player X is computer and player O is human")
    print("3 : player X is human and player O is computer")
    print("Player X always begins.")

main()
```