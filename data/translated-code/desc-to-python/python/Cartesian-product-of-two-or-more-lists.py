def nAryCartProd(lists):
    def cartesianProduct(a, b):
        return [x + (y,) for x in a for y in b]
    
    return functools.reduce(cartesianProduct, lists) if lists else [()]

import functools