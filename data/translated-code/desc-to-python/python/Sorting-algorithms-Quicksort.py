def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            _quicksort(arr, low, pivot - 1)
            _quicksort(arr, pivot + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quicksort(arr, 0, len(arr) - 1)