def combinations_of_length(elements, length, combination=[]):
    if length == 0:
        print(combination)
        return
    for i in range(len(elements)):
        new_combination = combination + [elements[i]]
        combinations_of_length(elements[i+1:], length-1, new_combination)