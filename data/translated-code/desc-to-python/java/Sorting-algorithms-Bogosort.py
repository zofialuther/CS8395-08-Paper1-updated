```python
import random

class BogoSort:
    def __init__(self, arr):
        self.arr = arr

    def bogo(self):
        shuffles = 0
        while not self.is_sorted():
            random.shuffle(self.arr)
            shuffles += 1
        print(f"Array sorted in {shuffles} shuffles")

    def is_sorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True

    def display_array(self):
        print(self.arr)

# Main method
if __name__ == "__main__":
    array = [5, 3, 8, 6, 2]
    sort = BogoSort(array)
    sort.bogo()
```