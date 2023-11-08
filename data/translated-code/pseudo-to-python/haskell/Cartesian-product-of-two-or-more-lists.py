def cartProdN(arrays):
    if len(arrays) == 0:
        return [[]]
    else:
        currentArray, *remainingArrays = arrays
        remainingProduct = cartProdN(remainingArrays)
        currentProduct = []
        for value in currentArray:
            for product in remainingProduct:
                currentProduct.append([value, *product])
        return currentProduct

print(cartProdN([[1776, 1789], [7,12], [4, 14, 23], [0,1]]))
print(cartProdN([[1,2,3], [30], [500, 100]]))
print(cartProdN([[1,2,3], [], [500, 100]]))