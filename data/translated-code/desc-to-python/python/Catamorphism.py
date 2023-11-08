from functools import reduce
import operator

listoflists = [['the', 'cat'], ['sat', 'on'], ['the', 'mat']]
concatenated_list = reduce(operator.add, listoflists)
print(concatenated_list)