import math

def main():
    print(entropy("1223334444"))

def entropy(items):
    grouped_items = sorted([(len(list(group)), key) for key, group in groupby(items)])
    fq_values = list(map(lambda x: x[0]/len(items), grouped_items))
    lg_values = list(map(lambda x: -x * math.log2(x), fq_values))
    result = sum(lg_values)
    return result