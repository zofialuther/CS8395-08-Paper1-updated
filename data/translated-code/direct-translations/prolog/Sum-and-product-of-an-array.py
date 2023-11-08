def sum(lst, result):
    if lst == []:
        return result
    else:
        return sum(lst[1:], result + lst[0])

def product(lst, result):
    if lst == []:
        return result
    else:
        return product(lst[1:], result * lst[0])