```python
class CartesianProduct:
    def product(self, lists):
        result = [[]]
        for lst in lists:
            temp = []
            for res in result:
                for item in lst:
                    temp.append(res + [item])
            result = temp
        return result

    def __init__(self):
        pass

    def __product(self, lists, idx, current, result):
        if idx == len(lists):
            result.append(current.copy())
            return
        for item in lists[idx]:
            current.append(item)
            self.__product(lists, idx + 1, current, result)
            current.pop()

    def main(self):
        lists = [[1, 2], [3, 4], [5, 6]]
        result = self.product(lists)
        for res in result:
            print(res)

cp = CartesianProduct()
cp.main()
```