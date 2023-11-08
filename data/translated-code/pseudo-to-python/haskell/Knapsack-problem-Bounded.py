def knapsack(items, cap):
    solu = foldr(f, listArray (0,cap) (repeat (0,[])), items)
    return solu[cap]

def f(item, ss):
    optimal = mapOptimal(ss, item)
    return listArray (0,cap) optimal

def mapOptimal(ss, item):
    maxVal = maximum(ss!ww, prepend(v*i, (name, i)) (ss!(ww - i*w)))
    return maxVal

print(knapsack(inv, 400))