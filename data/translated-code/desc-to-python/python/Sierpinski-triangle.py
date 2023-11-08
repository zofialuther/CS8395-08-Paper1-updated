def sierpinski(n):
    def sierpinski_pattern(n):
        if n == 0:
            return ['*']
        else:
            lower = sierpinski_pattern(n - 1)
            space = ' ' * (2 ** (n - 1))
            return [space.join(row) for row in zip(lower, lower)]
    
    def concatMap(func, lst):
        return ''.join(map(func, lst))
    
    result = concatMap(lambda x: x + '\n', sierpinski_pattern(n))
    print(result)

sierpinski(5)