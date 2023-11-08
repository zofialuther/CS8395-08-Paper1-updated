from array import array

def knapsack(items, cap):
    def solu(items):
        return foldr(f, array('i', [0] * (cap + 1)))

    def f(name, w, v, cnt, ss):
        def optimal(ww):
            return max(ss[ww], *[prepend((v*i, (name, i)), ss[ww - i*w]) for i in range(1, cnt+1) if i*w < ww])

        def prepend(x, y):
            return (x[0] + y[0], x[1] + [y[1]])

        return array('i', [optimal(ww) for ww in range(cap + 1)])

    return solu(items)[cap]

print(knapsack(inv, 400))