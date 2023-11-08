def egyptianQuotRem(m, n):
    def unfoldr(func, initState):
        result = []
        state = initState
        while True:
            res = func(state[0], state[1])
            if res is None:
                break
            else:
                result.append(res[0])
                state = res[1]
        return result
    
    def foldr(func, initState, arr):
        state = initState
        for item in arr[::-1]:
            state = func(item, state)
        return state
    
    rows = unfoldr(lambda i, x: (i, x) if x <= m else None, (1, n))
    print("Number pair unfolded to series of doubling rows:")
    print(rows)
    print("\nRows refolded down to (quot, rem):")
    print((0, m))
    
    def updateQuotRem(pair, quotRem):
        i, x = pair
        q, r = quotRem
        if x < r:
            print("({} + {}, -{}) -> rem {}".format(q, i, x, r-x))
            return (q + i, r - x)
        else:
            return (q, r)
    
    foldr(updateQuotRem, (0, m), rows)

egyptianQuotRem(580, 34)