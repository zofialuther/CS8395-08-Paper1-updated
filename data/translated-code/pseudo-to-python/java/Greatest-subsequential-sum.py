def BiggestSubsum(t):
    sum = 0
    maxsum = 0
    for i in range(len(t)):
        sum = sum + t[i]
        if sum < 0:
            sum = 0
        if sum > maxsum:
            maxsum = sum
    return maxsum