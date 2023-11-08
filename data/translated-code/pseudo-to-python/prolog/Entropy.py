```python
from math import log2

def shannon_entropy(s, entropy):
    cs = atom_chars(s)
    frequencies = relative_frequencies(cs)
    c_is = [f * log2(f) for _, f in frequencies]
    e = sum(c_is)
    entropy = -e

def relative_frequencies(lst):
    rle = run_length_encoding(lst)
    sorted_rle = sorted(rle, key=lambda x: x[1])
    elements_run_lengths = {k: sum(v) for k, v in group_pairs_by_key(sorted_rle).items()}
    elements_in_list = len(lst)
    frequencies = [(e, rl / elements_in_list) for e, rl in elements_run_lengths.items()]
    return frequencies

def run_length_encoding(lst):
    if not lst:
        return []
    else:
        rle = []
        run_length_encoding_helper(lst, [(lst[0], 1)], rle)
        return rle

def run_length_encoding_helper(lst, fs, acc):
    if not lst:
        acc.extend(fs)
    else:
        if lst[0] == fs[-1][0]:
            f = fs[-1][1] + 1
            run_length_encoding_helper(lst[1:], [(lst[0], f)], acc)
        else:
            run_length_encoding_helper(lst[1:], fs + [(lst[0], 1)], acc)

def group_pairs_by_key(lst):
    d = {}
    for k, v in lst:
        d[k] = d.get(k, []) + [v]
    return d
```