def bSearch(p, low, high):
    if high < low:
        return None
    else:
        mid = (low + high) // 2
        result = p(mid)
        if result == "LT":
            return bSearch(p, low, mid - 1)
        elif result == "GT":
            return bSearch(p, mid + 1, high)
        elif result == "EQ":
            return mid

def bSearchArray(a, x):
    low = 0
    high = len(a) - 1
    p = lambda i: "LT" if x < a[i] else ("GT" if x > a[i] else "EQ")
    return bSearch(p, low, high)

axs = ["alpha", "beta", "delta", "epsilon", "eta", "gamma", "iota", "kappa", "lambda", "mu", "theta", "zeta"]

def main():
    e = "mu"
    found = bSearchArray(axs, e)
    if found == None:
        print("' : " + e + "' Not found")
    else:
        print("' : " + e + "' found at index " + str(found))

main()