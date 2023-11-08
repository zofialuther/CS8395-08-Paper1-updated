def insertionSort(arr):
    import Data.List
    return foldr(insert, [], arr)
  
# Example use
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = insertionSort(arr)
print(sorted_arr) # Output: [1, 1, 2, 3, 4, 5, 6, 9]