def count_jewels(Stones, Jewels, N):
    stones_list = [ord(c) for c in Stones]
    jewels_list = [ord(c) for c in Jewels]
    stones_list.sort()
    jewels_list.sort()
    
    count_jewels_helper(stones_list, jewels_list, N)

def count_jewels_helper(stones_list, jewels_list, N):
    # helper predicate to count the occurrences of jewels in stones
    # iterate through the sorted lists and count the occurrences
    # return the count in the N variable
    pass  # implementation of the helper predicate is not provided in the given description