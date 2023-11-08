from functools import reduce

def nAryCartProd(xxs):
    def cartesianProduct(a, b):
        return [x + y for x in a for y in b]
    
    return reduce(cartesianProduct, xxs)