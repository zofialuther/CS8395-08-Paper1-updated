def combinationsWithRepetition(k, xs):
    result = []
    if k == 0:
        return result
    else:
        temp = []
        for i in range(len(xs)):
            current = combinationsWithRepetition(k - 1, xs)
            for j in range(len(current)):
                current[j].append(xs[i])
                temp.append(current[j])
        return temp

def main():
    print(combinationsWithRepetition(2, ["iced", "jam", "plain"]))
    lengthResult = len(combinationsWithRepetition(3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(lengthResult)