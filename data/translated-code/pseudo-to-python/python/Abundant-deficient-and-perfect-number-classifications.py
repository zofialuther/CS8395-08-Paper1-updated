def nthArrow(f):
    def go(v, n):
        m = n - 1
        if n > len(v):
            return v
        else:
            result = []
            for i in range(len(v)):
                if m != i:
                    result.append(v[i])
                else:
                    result.append(f(v[i]))
            return result
    
    return lambda tpl: lambda n: go(tpl, n)