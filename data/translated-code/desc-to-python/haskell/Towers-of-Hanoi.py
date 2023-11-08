def hanoiIO(n):
    moves = hanoi(n)
    mapM_(f, moves)

def f(move):
    disk, start, end = move
    print(f"Move disk {disk} from peg {start} to peg {end}")