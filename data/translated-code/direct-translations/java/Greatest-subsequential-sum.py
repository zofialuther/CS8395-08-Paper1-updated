def biggest_subsum(t):
    sum = 0
    maxsum = 0
    for i in t:
        sum += i
        if sum < 0:
            sum = 0
        maxsum = max(sum, maxsum)
    return maxsum