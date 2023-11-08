def cartProdN(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for x in lst[0]:
            for y in cartProdN(lst[1:]):
                result.append([x] + y)
        return result

print(cartProdN([[1776, 1789], [7,12], [4, 14, 23], [0,1]]))
print(cartProdN([[1,2,3], [30], [500, 100]]))
print(cartProdN([[1,2,3], [], [500, 100]])