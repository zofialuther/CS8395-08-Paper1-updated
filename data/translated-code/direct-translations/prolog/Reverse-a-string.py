def accRev(lst, acc, result):
    if len(lst) > 0:
        accRev(lst[1:], [lst[0]] + acc, result)
    else:
        result = acc

def rev(lst):
    result = []
    accRev(lst, [], result)
    return result