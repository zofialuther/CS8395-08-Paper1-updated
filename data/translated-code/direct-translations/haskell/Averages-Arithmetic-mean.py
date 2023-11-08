from statistics import mean

def calculate_mean(arr):
    if not arr:
        return 0
    return mean(arr)