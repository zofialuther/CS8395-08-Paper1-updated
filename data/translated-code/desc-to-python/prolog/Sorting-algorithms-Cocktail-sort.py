```python
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1

def cocktail(arr):
    cocktail_sort(arr)

def test():
    sample_input = [3, 1, 5, 2, 4]
    cocktail(sample_input)
    print(sample_input)

test()
```