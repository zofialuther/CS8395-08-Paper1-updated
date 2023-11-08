import Data.Array

def ordSuffs():
    return ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]

def ordSuff(n):
    def suff(m):
        if m % 100 >= 11 and m % 100 <= 13:
            return "th"
        else:
            return ordSuffs()[m % 10]
    return str(n) + suff(n)

def printOrdSuffs(lst):
    result = ' '.join(map(ordSuff, lst))
    print(result)

def main():
    printOrdSuffs(list(range(0, 26)))
    printOrdSuffs(list(range(250, 266)))
    printOrdSuffs(list(range(1000, 1026))