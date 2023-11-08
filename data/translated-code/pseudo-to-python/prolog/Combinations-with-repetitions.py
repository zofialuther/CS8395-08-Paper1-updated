def combinations_of_length(lst, result):
    if not lst:
        return
    else:
        result.append(lst)
        combinations_of_length(lst[:], result)
        lst.pop()
        combinations_of_length(lst[:], result)