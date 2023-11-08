from functools import reduce

def nAryCartProd(xxs):
    return reduce(cartesianProduct, xxs)