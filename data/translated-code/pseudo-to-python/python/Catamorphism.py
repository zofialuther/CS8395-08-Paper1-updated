from operator import add

listoflists = [['the', 'cat'], ['sat', 'on'], ['the', 'mat']]

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

result = reduce(add, listoflists, [])
print(result)