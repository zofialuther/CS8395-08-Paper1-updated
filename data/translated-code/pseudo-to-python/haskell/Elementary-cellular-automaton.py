def rule(n, l, x, r):
    result = n // (2**(4*l + 2*x + r)) % 2
    return result

def initial(n):
    array = list(range(n))
    
    def padRight(n, lst):
        while len(lst) < n:
            lst.append(0)
        return lst
    
    def center(lst, n):
        start = (len(lst) - n) // 2
        return lst[start:start+n]