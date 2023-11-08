def member1(X, lst):
    if not lst:
        return False
    if X == lst[0]:
        return True
    return member1(X, lst[1:])

def distinct(lst, result):
    if not lst:
        return result
    if member1(lst[0], lst[1:]):
        return distinct(lst[1:], result)
    else:
        return distinct(lst[1:], result + [lst[0]])