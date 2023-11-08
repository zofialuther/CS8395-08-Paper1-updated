def extractRange(list):
    result = ','.join(f(list))
    return result

def f(list):
    result = []
    if len(list) >= 3:
        if list[0] + 1 == list[1] and list[1] + 1 == list[2]:
            rangeStart = list[0]
            rangeEnd, remainingList = g(list[2] + 1, list[3:])
            result.append(str(rangeStart) + "-" + str(rangeEnd))
            result += f(remainingList)
        else:
            result.append(str(list[0]))
            result += f(list[1:])
    elif len(list) == 2:
        result.append(str(list[0]))
        result += f(list[1:])
    return result

def g(start, list):
    if start == list[0]:
        return g(start + 1, list[1:])
    else:
        return start - 1, list