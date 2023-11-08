class BogoSort:
    def main(arr):
        arr = [4,5,6,0,7,8,9,1,2,3]
        now = BogoSort()
        print("Unsorted: ", end="")
        now.display1D(arr)
        now.bogo(arr)
        print("Sorted: ", end="")
        now.display1D(arr)

    def bogo(arr):
        shuffle = 1
        while not isSorted(arr):
            shuffle += 1
            shuffle(arr)
        print("This took", shuffle)

    def shuffle(arr):
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            swap(arr, i, j)

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def isSorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def display1D(arr):
        for num in arr:
            print(num, end=" ")
        print()