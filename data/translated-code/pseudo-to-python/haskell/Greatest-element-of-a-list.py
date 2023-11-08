from Data.List import maximumBy
from Data.Ord import comparing

wds = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]

def main():
    result = maximumBy(comparing(len), wds)
    print(result)