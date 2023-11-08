def concat(arrayA, arrayB):
    list = []
    for value in arrayA:
        list.append(value)
    for value in arrayB:
        list.append(value)
    array = [0] * len(list)
    for index in range(len(list)):
        array[index] = list[index]
    return array