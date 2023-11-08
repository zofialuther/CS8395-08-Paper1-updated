def removeDuplicates(values):
    list = []
    for value in values:
        if value not in list:
            list.append(value)
    newValues = [0] * len(list)
    index = 0
    for value in list:
        newValues[index] = value
        index += 1
    return newValues