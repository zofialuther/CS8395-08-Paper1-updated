def select(list, prompt):
    if len(list) == 0:
        return ""
    sc = input()
    ret = None
    while ret is None:
        for i in range(len(list)):
            print(i, list[i])
        print(prompt)
        index = int(input())
        if index >= 0 and index < len(list):
            ret = list[index]
    return ret