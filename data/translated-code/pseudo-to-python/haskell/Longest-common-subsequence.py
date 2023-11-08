from Data.Ord import *
from Data.List import *

def lcs(xs, ys):
    def subsequences(xs):
        return [xs[i:j] for i in range(len(xs)) for j in range(i+1, len(xs)+1)]
    
    def intersection(lst1, lst2):
        return list(set(lst1) & set(lst2))
    
    sub_xs = subsequences(xs)
    sub_ys = subsequences(ys)
    common_subs = intersection(sub_xs, sub_ys)
    lcs = max(common_subs, key=len)
    return lcs

def main():
    result = lcs("thisisatest", "testing123testing")
    print(result)

main()