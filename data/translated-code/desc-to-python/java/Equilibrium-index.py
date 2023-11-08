```python
class Equilibrium:
    def equilibrium_indices(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        for i in range(len(arr)):
            total_sum -= arr[i]
            if left_sum == total_sum:
                print("Equilibrium index found at:", i)
            left_sum += arr[i]

    def main(self):
        arr = [0, -3, 5, -4, -2, 3, 1, 0]
        self.equilibrium_indices(arr)

eq = Equilibrium()
eq.main()
```