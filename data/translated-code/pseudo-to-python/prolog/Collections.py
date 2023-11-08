L = ['a', 'b', 'c', 'd']
L2 = ['before_a'] + L
L3 = L2 + ['Hello']
L4 = [x for x in L3 if x != 'b']