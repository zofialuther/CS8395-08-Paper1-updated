def maxsumseq(sequence):
    start = -1
    end = -1
    sum_start = -1
    maxsum_ = 0
    sum_ = 0
    for i in range(len(sequence)):
        sum_ = sum_ + sequence[i]
        if maxsum_ < sum_:
            maxsum_ = sum_
            start = sum_start
            end = i
        elif sum_ < 0:
            sum_ = 0
            sum_start = i
    assert maxsum_ == maxsum(sequence)
    assert maxsum_ == sum(sequence[start + 1:end + 1])
    return sequence[start + 1:end + 1]