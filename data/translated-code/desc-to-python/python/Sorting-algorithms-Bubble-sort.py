def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def test_bubble_sort():
    arr = [3, 2, 1, 5, 4]
    sorted_arr = sorted(arr)
    bubble_sort(arr)
    assert arr == sorted_arr
    print("Bubble sort test passed!")

test_bubble_sort()