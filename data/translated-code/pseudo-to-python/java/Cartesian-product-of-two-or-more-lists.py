class CartesianProduct:
  def product(lists):
    product = []
    product(product, [], lists)
    return product

  def product(result, existingTupleToComplete, valuesToUse):
    for value in valuesToUse[0]:
      newExisting = existingTupleToComplete.copy()
      newExisting.append(value)
      if len(valuesToUse) == 1:
        result.append(newExisting)
      else:
        newValues = []
        for i in range(1, len(valuesToUse)):
          newValues.append(valuesToUse[i])
        product(result, newExisting, newValues)

list1 = [1776, 1789]
list2 = [7, 12]
list3 = [4, 14, 23]
list4 = [0, 1]
input = [list1, list2, list3, list4]
cartesianProduct = CartesianProduct()
product = cartesianProduct.product(input)
print(product)