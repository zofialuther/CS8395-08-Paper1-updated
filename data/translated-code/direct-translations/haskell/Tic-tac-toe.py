```python
import random
from typing import List, Tuple, Union

def tictactoe(a: str) -> bool:
    return tictactoeFor('X', a) != tictactoeFor('O', a)

def tictactoeFor(n: str, s: str) -> bool:
    a, b, c, d, e, f, g, h, i = s
    return [n, n, n] in [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]

start = "         "

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
            return (moves, player, game)
    elif moves == 9 or tictactoeFor(player, game):
        return (moves, player, game)
    else:
        otherPlayer = 'O' if player == 'X' else 'X'
        result = place(i, otherPlayer, game)
        if isinstance(result, str):
            return developGame(iterateMore, moves, i + 1, otherPlayer, game)
        else:
            return developGame(iterateMore, moves + 1, 0, otherPlayer, result)

def bestMoveFor(player: str, game: str) -> int:
    continuations = [(x, developGame(True, 0, x, player, game)) for x in range(9)]
    move = lambda x: x[1][0]
    bestMove, _ = min(continuations, key=move)
    return bestMove

def canBlock(p: str, s: str) -> Union[str, int]:
    a, b, c, d, e, f, g, h, i = s
    cells = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, g]]
    for xs in cells:
        if xs.count(p) == 2 and xs.count(' ') == 1:
            x = xs.index(' ')
            if x in range(9):
                return x
    return ''

def showGame(s: str) -> str:
    a, b, c, d, e, f, g, h, i = s
    topBottom = "+----+---+---+---+\n"
    row = lambda n, x: "| " + n + "+ | " + " | ".join(x) + " |\n" + topBottom
    return (topBottom + "|    | 1 | 2 | 3 |\n" + topBottom + 
            row("0", [a, b, c]) + row("3", [d, e, f]) + row("6", [g, h, i]))

def enterNumber() -> int:
    c = input()
    if c in "123456789":
        return int(c)
    else:
        print("\nPlease enter a digit!")
        return enterNumber()

def turn(count: int, player: str, game: str) -> Tuple[int, str, str]:
    print(f"Please tell me where you want to put an {player}: ")
    pos = enterNumber()
    result = place(pos - 1, player, game)
    if isinstance(result, str):
        return count + 1, 'O' if player == 'X' else 'X', result
    else:
        print("That place is already taken!\n")
        return turn(count, player, result)

def changePlayer(player: str) -> str:
    return 'O' if player == 'X' else 'X'

def autoTurn(forceRandom: bool, count: int, player: str, game: str) -> Tuple[int, str, str]:
    i = random.randint(0, 8) if count == 0 or forceRandom else canBlock(player, game) if canBlock(player, game) != '' else bestMoveFor(player, game)
    result = place(i, player, game)
    if isinstance(result, str):
        print(f"It's player {player}'s turn.")
        return count + 1, changePlayer(player), result
    else:
        return autoTurn(True, count, player, result)

def play(auto: int, count: int, player: str, game: str) -> None:
    newCount, newPlayer, newGame = autoTurn(False, count, player, game) if auto in [1, 2, 3] else turn(count, player, game)
    print("\n" + showGame(newGame))
    if tictactoe(newGame):
        print(f"Player {changePlayer(newPlayer)} wins!\n")
    elif newCount == 9:
        print("Draw!\n")
    else:
        play(auto, newCount, newPlayer, newGame)

def main() -> None:
    a = input()
    if not a:
        usage()
    else:
        option = a[0]
        if option in ["0", "1", "2", "3"]:
            print("\n" + showGame(start))
            m = int(option)
            play(m, 0, 'X', start)
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

if __name__ == "__main__":
    main()
```