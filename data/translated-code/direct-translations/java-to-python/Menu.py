def select(list, prompt):
    if len(list) == 0:
        return ""
    ret = None
    while ret is None:
        for i in range(len(list)):
            print(i, ": ", list[i])
        index = int(input(prompt))
        if index >= 0 and index < len(list):
            ret = list[index]
    return ret