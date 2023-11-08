def ffr(n):
    rl = [1]
    n_ = 1
    x = 2
    while len(rl) < n:
        n_ = n_ + x
        rl.append(n_)
        x = next_number_in_sequence
    return rl[n - 1]

def ffs(n):
    rl = [2]
    n_ = 1
    x = 2
    while len(rl) <= n:
        n_ = n_ + x
        rl.append(n_)
        x = next_number_in_sequence
    return rl[n]

def main():
    print(ffr(1), ffr(2), ..., ffr(10))
    i1000 = sorted([ffr(1), ffr(2), ..., ffr(40) + ffs(1), ffs(2), ..., ffs(960)])
    print(i1000 == [1, 2, ..., 1000])