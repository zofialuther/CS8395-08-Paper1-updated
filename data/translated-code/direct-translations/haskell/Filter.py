import array

ary = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
evens = array.array('i', [x for x in ary if x % 2 == 0])