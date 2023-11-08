def lis(In, Out):
    def one_is(lst, current, final):
        if not lst:
            final.extend(current)
        else:
            h, *t = lst
            if not current or h > current[-1]:
                one_is(t, current + [h], final)
            one_is(t, current, final)
    
    N = []
    Is = []
    for i in range(len(In)):
        current = []
        final = []
        one_is(In[i:], current, final)
        N.append(len(final))
        Is.append(final)
    
    max_len = max(N)
    max_idx = N.index(max_len)
    Res = Is[max_idx]
    Out.extend(Res[::-1])