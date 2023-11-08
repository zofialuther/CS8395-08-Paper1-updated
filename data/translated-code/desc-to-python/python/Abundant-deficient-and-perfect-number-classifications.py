def nthArrow(f):
    def new_function(tuple, n):
        if n < 0 or n >= len(tuple):
            return tuple
        else:
            return tuple[:n] + (f(tuple[n]),) + tuple[n+1:]
    return new_function