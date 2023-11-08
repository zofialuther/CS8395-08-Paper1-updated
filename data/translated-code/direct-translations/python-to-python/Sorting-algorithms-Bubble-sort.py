def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq

if __name__ == "__main__":
    from random import shuffle

    testset = [_ for _ in range(100)]
    testcase = testset.copy()
    shuffle(testcase)
    assert testcase != testset
    bubble_sort(testcase)
    assert testcase == testset