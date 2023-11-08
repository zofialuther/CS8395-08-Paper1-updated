from numpy import array, pad

def rule(n, l, x, r):
    return n // (2**(4*l + 2*x + r)) % 2

def initial(n):
    lst = array(range(n))
    lst = pad(lst, (0, n - len(lst)), mode='constant', constant_values=0)
    lst = lst[len(lst)//2+1:] + lst[:len(lst)//2+1]
    return lst