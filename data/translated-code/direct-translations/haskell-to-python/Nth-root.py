def nthRoot(n, x):
    result = until(lambda pair: pair[0] == pair[1], 
                   lambda pair: (pair[1], ((n-1)*pair[1]+x/pair[1]**(n-1))/n), 
                   (x,x/n))
    return result[0]