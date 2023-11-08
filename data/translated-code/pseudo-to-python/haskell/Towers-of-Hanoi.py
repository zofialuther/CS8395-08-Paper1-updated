def hanoiIO(n):
    towers = hanoi(n, 1, 2, 3)
    for move in towers:
        print("Move " + str(move.x) + " to " + str(move.y))