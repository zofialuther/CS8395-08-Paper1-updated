def solution(board):
    if len(board) == 0:
        return True
    else:
        x, y = board[0]
        others = board[1:]
        return solution(others) and (y in [1,2,3,4,5,6,7,8]) and noattack(x, y, others)

def noattack(x, y, board):
    if len(board) == 0:
        return True
    else:
        x1, y1 = board[0]
        others = board[1:]
        return (y != y1) and (y1 - y != x1 - x) and (y1 - y != x - x1) and noattack(x, y, others)

def member(item, lst):
    if len(lst) == 0:
        return False
    else:
        first, rest = lst[0], lst[1:]
        return (item == first) or member(item, rest)

def template():
    return [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)]