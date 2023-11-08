def sort(nums):
    for currentPlace in range(len(nums)):
        smallest = float('inf')
        smallestAt = currentPlace
        for check in range(currentPlace, len(nums)):
            if nums[check] < smallest:
                smallestAt = check
                smallest = nums[check]
        temp = nums[currentPlace]
        nums[currentPlace] = nums[smallestAt]
        nums[smallestAt] = temp