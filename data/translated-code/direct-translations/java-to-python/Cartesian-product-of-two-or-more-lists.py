```python
class CartesianProduct:
    def product(self, lists):
        product = []
        self._product(product, [], lists)
        return product

    def _product(self, result, existingTupleToComplete, valuesToUse):
        if not valuesToUse:
            result.append(existingTupleToComplete)
        else:
            for value in valuesToUse[0]:
                newExisting = existingTupleToComplete + [value]
                self._product(result, newExisting, valuesToUse[1:])

if __name__ == "__main__":
    list1 = [1776, 1789]
    list2 = [7, 12]
    list3 = [4, 14, 23]
    list4 = [0, 1]

    input_lists = [list1, list2, list3, list4]

    cartesian_product = CartesianProduct()
    product = cartesian_product.product(input_lists)
    print(product)
```