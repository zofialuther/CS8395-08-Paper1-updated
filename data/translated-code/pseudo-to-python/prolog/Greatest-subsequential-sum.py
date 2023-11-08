def subseq(sub, seq):
    for i in range(len(seq)):
        suffix = seq[i:]
        for j in range(len(suffix)):
            prefix = suffix[:j+1]
            if prefix == sub:
                return True
    return False

def maxsubseq(lst, sub, sum):
    subs = [lst[i:j+1] for i in range(len(lst)) for j in range(i, len(lst))]
    sums = [sum(sub) for sub in subs]
    max_sum = max(sums)
    max_index = sums.index(max_sum)
    sub = subs[max_index]
    return sub, max_sum