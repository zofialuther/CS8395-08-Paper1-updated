def inconsistentChar(xs):
    if len(xs) == 0:
        return None
    else:
        index = xs.index(next((item for item in xs if item != xs[0]), -1))
        if index != -1:
            return [index, xs[index]]
        else:
            return None