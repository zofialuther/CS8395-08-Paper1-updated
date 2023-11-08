def permutations(lst):
    def ins(x, xs, n):
        firstHalf = xs[:n]
        secondHalf = xs[n:]
        return firstHalf + [x] + secondHalf

    result = [[]]

    for i in range(len(lst)):
        x = lst[i]
        temp = []
        for j in range(len(result) + 1):
            temp.append(ins(x, result[j], j))
        result = temp

    return result

def main():
    print(permutations([1, 2, 3]))

main()