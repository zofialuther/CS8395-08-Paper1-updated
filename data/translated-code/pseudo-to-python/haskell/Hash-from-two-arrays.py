from collections import defaultdict

def makeMap(keys, values):
    return dict(zip(keys, values))

mymap = makeMap(['a', 'b', 'c'], [1, 2, 3])