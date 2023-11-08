def solution(board):
    if len(board) == 0:
        return True
    else:
        x, y = board[0]
        others = board[1:]
        if solution(others) and y in [1,2,3,4,5,6,7,8] and no_attack(x, y, others):
            return True
        else:
            return False

def no_attack(x, y, others):
    if len(others) == 0:
        return True
    else:
        x1, y1 = others[0]
        if y != y1 and abs(y1 - y) != abs(x1 - x) and abs(y1 - y) != abs(x - x1):
            return no_attack(x, y, others[1:])
        else:
            return False

def member(item, lst):
    if len(lst) == 0:
        return False
    elif item == lst[0]:
        return True
    else:
        return member(item, lst[1:])

template = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]