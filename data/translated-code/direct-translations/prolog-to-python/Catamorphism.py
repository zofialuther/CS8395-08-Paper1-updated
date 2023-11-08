def foldr(Foldy, items, starter, acc_up):
    if len(items) > 0:
        acc_up_prev = foldr(Foldy, items[1:], starter, acc_up)
        acc_up = Foldy(items[0], acc_up_prev)
    else:
        acc_up = starter
    return acc_up
