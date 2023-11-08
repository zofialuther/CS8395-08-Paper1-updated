from Data.Array import Array, Ix, listArray, bounds

# BINARY SEARCH
def bSearch(p, low, high):
    if high < low:
        return None
    else:
        mid = (low + high) // 2
        if p(mid) < 0:
            return bSearch(p, low, mid - 1)
        elif p(mid) > 0:
            return bSearch(p, mid + 1, high)
        else:
            return mid

# Application to an array
def bSearchArray(a, x):
    def compare_func(y):
        return compare(x, a[y])
    return bSearch(compare_func, *bounds(a))

# TEST
def main():
    axs = listArray(0, 11, [
        "alpha",
        "beta",
        "delta",
        "epsilon",
        "eta",
        "gamma",
        "iota",
        "kappa",
        "lambda",
        "mu",
        "theta",
        "zeta"
    ])
    e = "mu"
    found = bSearchArray(axs, e)
    if found is None:
        print("'" + e + "' Not found")
    else:
        print("'" + e + "' found at index " + str(found))

main()