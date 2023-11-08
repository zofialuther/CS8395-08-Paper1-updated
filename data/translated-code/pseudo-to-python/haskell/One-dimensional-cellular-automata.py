def bnd(string):
    if string == "_##":
        return '#'
    elif string == "#_#":
        return '#'
    elif string == "##_":
        return '#'
    else:
        return '_'

def nxt(string):
    def go(array):
        if len(array) == 2:
            return None
        else:
            return (bnd(array[:3]), array[1:])
    return unfoldr(go, '_' + string + '_')

def lahmahgaan(string):
    result = []
    while string[-1] != result[-2][-1]:
        result.append(nxt(result[-1]))
    return result

def main():
    gen = newStdGen()
    randomList = randomList = [random.choice([0,1]) for _ in range(36)]
    mappedList = list(map(lambda x: '_#' if x == 0 else '#_', randomList))
    output = list(map(lahmahgaan, mappedList))
    for elem in output:
        print(elem)