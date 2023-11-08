def binarySearch(nums, check):
    hi = len(nums) - 1
    lo = 0
    while hi >= lo:
        guess = (lo + hi) // 2
        if nums[guess] > check:
            hi = guess - 1
        elif nums[guess] < check:
            lo = guess + 1
        else:
            return guess
    return -1

def main(args):
    haystack = [1, 5, 6, 7, 8, 11]
    needle = 5
    index = binarySearch(haystack, needle)
    if index == -1:
        print(str(needle) + " is not in the array")
    else:
        print(str(needle) + " is at index " + str(index))