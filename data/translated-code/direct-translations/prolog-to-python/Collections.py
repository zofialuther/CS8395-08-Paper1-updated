# create a list
L = ['a', 'b', 'c', 'd']

# prepend to the list
L2 = ['before_a'] + L

# append to the list
L3 = L2 + ['Hello']

# delete from list
L4 = [x for x in L3 if x != 'b']