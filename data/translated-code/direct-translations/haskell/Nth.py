import numpy as np

ordSuffs = {
    0: "th", 1: "st", 2: "nd", 3: "rd", 4: "th",
    5: "th", 6: "th", 7: "th", 8: "th", 9: "th"
}

def ordSuff(n):
    return str(n) + suff(n)

def suff(m):
    if (m % 100) >= 11 and (m % 100) <= 13:
        return "th"
    else:
        return ordSuffs[m % 10]

def printOrdSuffs(arr):
    print(' '.join(map(ordSuff, arr)))

if __name__ == "__main__":
    printOrdSuffs(np.arange(0, 26))
    printOrdSuffs(np.arange(250, 266))
    printOrdSuffs(np.arange(1000, 1026))