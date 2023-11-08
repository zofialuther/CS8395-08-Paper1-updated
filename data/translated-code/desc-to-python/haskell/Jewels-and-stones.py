def jewelCount(list1, list2):
    def go(x, y):
        return x + 1 if y in list1 else x

    return foldr(go, list2, 0)

def foldr(func, lst, acc):
    if not lst:
        return acc
    else:
        return func(lst[-1], foldr(func, lst[:-1], acc))

def main():
    print(jewelCount([1, 2, 3, 4], [2, 4, 6, 8]))  # Output: 2
    print(jewelCount([5, 6, 7, 8], [1, 2, 3, 4]))  # Output: 0

main()