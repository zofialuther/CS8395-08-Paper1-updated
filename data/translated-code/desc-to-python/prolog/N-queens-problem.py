def solution(queens):
    def attack((x1, y1), (x2, y2)):
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

    def iterate(queens):
        if len(queens) <= 1:
            return True
        else:
            for q in queens[1:]:
                if attack(queens[0], q):
                    return False
            return iterate(queens[1:])

    def member(y):
        return 1 <= y <= 8

    def template(x):
        return [(x, y) for y in range(1, 9)]

    return iterate(queens)