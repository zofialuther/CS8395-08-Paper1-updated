def in_order(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True