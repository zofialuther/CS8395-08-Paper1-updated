from random import randint

class Choice:
    Rock = 1
    Paper = 2
    Scissors = 3

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
    h = input("rock, paper or scissors?").lower()
    if h == "scissors":
        return Choice.Scissors
    elif h == "rock":
        return Choice.Rock
    elif h == "paper":
        return Choice.Paper
    else:
        raise ValueError("invalid input")

def game(r, p, s):
    print("rock, paper or scissors?")
    h = getrps()
    c = genrps(r, p, s)
    print("Player: " + str(h) + " Computer: " + str(c))
    if beats(h, c):
        print("player wins\n")
    elif beats(c, h):
        print("player loses\n")
    else:
        print("draw\n")
    rr = r + 1 if h == Choice.Rock else r
    pp = p + 1 if h == Choice.Paper else p
    ss = s + 1 if h == Choice.Scissors else s
    game(rr, pp, ss)

game(1, 1, 1)