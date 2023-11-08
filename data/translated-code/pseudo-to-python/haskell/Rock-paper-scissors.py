```python
from random import randint

class Choice:
    Rock = 0
    Paper = 1
    Scissors = 2

def beats(h, c):
    if (h == Choice.Paper and c == Choice.Rock) or (h == Choice.Scissors and c == Choice.Paper) or (h == Choice.Rock and c == Choice.Scissors):
        return True
    else:
        return False

def genrps(r, p, s):
    x = randint(1, r + p + s)
    if x <= s:
        return Choice.Rock
    elif x <= s + r:
        return Choice.Paper
    else:
        return Choice.Scissors

def getrps():
    input_str = input("rock, paper or scissors? ")
    if input_str == "scissors":
        return Choice.Scissors
    elif input_str == "rock":
        return Choice.Rock
    elif input_str == "paper":
        return Choice.Paper
    else:
        raise ValueError("Invalid input")

def game(r, p, s):
    print("rock, paper or scissors?")
    h = getrps()
    c = genrps(r, p, s)
    print("Player: " + str(h) + " Computer: " + str(c))
    print("player wins" if beats(h, c) else "player loses" if beats(c, h) else "draw")
    rr = r + 1 if h == Choice.Rock else r
    pp = p + 1 if h == Choice.Paper else p
    ss = s + 1 if h == Choice.Scissors else s
    game(rr, pp, ss)

game(1, 1, 1)
```