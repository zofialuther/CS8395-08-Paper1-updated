class BogoSort:
    def main(self, args):
        # Enter array to be sorted here
        arr = [4, 5, 6, 0, 7, 8, 9, 1, 2, 3]

        now = BogoSort()
        print("Unsorted: ", end='')
        now.display1D(arr)

        now.bogo(arr)

        print("Sorted: ", end='')
        now.display1D(arr)

    def bogo(self, arr):
        # Keep a track of the number of shuffles
        shuffle = 1
        while not self.isSorted(arr):
            self.shuffle(arr)
            shuffle += 1
        # Boast
        print("This took " + str(shuffle) + " shuffles.")

    def shuffle(self, arr):
        # Standard Fisher-Yates shuffle algorithm
        i = len(arr) - 1
        while i > 0:
            self.swap(arr, i, int((i * 0.5)))
            i -= 1

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def isSorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    def display1D(self, arr):
        for i in range(len(arr)):
            print(arr[i], end=' ')
        print()

# Create an instance of the BogoSort class and call the main method
bogo = BogoSort()
bogo.main(None)