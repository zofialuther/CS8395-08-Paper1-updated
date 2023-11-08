```python
class PermutationSort:
    def main(self):
        a = [3, 2, 1, 8, 9, 4, 6]
        print("Unsorted: {}".format(a))
        a = self.pSort(a)
        print("Sorted: {}".format(a))

    def pSort(self, a):
        list = []
        self.permute(a, len(a), list)
        for x in list:
            if self.isSorted(x):
                return x
        return a

    def permute(self, a, n, list):
        if n == 1:
            b = a.copy()
            list.append(b)
            return
        for i in range(n):
            self.swap(a, i, n-1)
            self.permute(a, n-1, list)
            self.swap(a, i, n-1)

    def isSorted(self, a):
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                return False
        return True

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

ps = PermutationSort()
ps.main()
```