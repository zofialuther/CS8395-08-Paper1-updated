from functools import reduce
from operator import add

listoflists = [['the', 'cat'], ['sat', 'on'], ['the', 'mat']]
result = reduce(add, listoflists, [])
print(result) # Output: ['the', 'cat', 'sat', 'on', 'the', 'mat']