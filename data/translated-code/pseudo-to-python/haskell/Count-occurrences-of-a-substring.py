def count(sub, lst):
    result = 0
    for element in lst:
        if element.startswith(sub):
            result += 1
    return result