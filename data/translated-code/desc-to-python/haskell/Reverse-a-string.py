def rev(accumulator, item):
    return [item] + accumulator

def accumulatingReverse(input_list):
    return foldl(rev, input_list, [])

# assuming foldl function is already defined
# rest of the code is not provided so can't be translated.