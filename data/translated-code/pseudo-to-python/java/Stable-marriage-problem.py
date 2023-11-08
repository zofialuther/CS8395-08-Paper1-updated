from collections import deque

def match(guys, guyPrefers, girlPrefers):
    engagedTo = {}
    freeGuys = deque(guys)
    while freeGuys:
        thisGuy = freeGuys.popleft()
        thisGuyPrefers = guyPrefers[thisGuy]
        for girl in thisGuyPrefers:
            if girl not in engagedTo:
                engagedTo[girl] = thisGuy
                break
            else:
                otherGuy = engagedTo[girl]
                thisGirlPrefers = girlPrefers[girl]
                if thisGirlPrefers.index(thisGuy) < thisGirlPrefers.index(otherGuy):
                    engagedTo[girl] = thisGuy
                    freeGuys.append(otherGuy)
                    break
    return engagedTo

def checkMatches(guys, girls, matches, guyPrefers, girlPrefers):
    if not set(matches.keys()).issuperset(set(girls)):
        return False
    if not set(matches.values()).issuperset(set(guys)):
        return False
    invertedMatches = {v: k for k, v in matches.items()}
    for couple in matches.items():
        shePrefers = girlPrefers[couple[0]]
        sheLikesBetter = shePrefers[:shePrefers.index(couple[1])]
        hePrefers = guyPrefers[couple[1]]
        heLikesBetter = hePrefers[:hePrefers.index(couple[0])]
        for guy in sheLikesBetter:
            guysFinace = invertedMatches[guy]
            thisGuyPrefers = guyPrefers[guy]
            if thisGuyPrefers.index(guysFinace) > thisGuyPrefers.index(couple[0]):
                print(couple[0] + " likes " + guy + " better than " + couple[1] + " and " + guy + " likes " + couple[0] + " better than their current partner")
                return False
        for girl in heLikesBetter:
            girlsFinace = matches[girl]
            thisGirlPrefers = girlPrefers[girl]
            if thisGirlPrefers.index(girlsFinace) > thisGirlPrefers.index(couple[0]):
                print(couple[1] + " likes " + girl + " better than " + couple[0] + " and " + girl + " likes " + couple[1] + " better than their current partner")
                return False
    return True

guys = ["abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"]
girls = ["abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"]
guyPrefers = {}
girlPrefers = {}
matches = match(guys, guyPrefers, girlPrefers)
for couple in matches.items():
    print(couple[0] + " is engaged to " + couple[1])
if checkMatches(guys, girls, matches, guyPrefers, girlPrefers):
    print("Marriages are stable")
else:
    print("Marriages are unstable")
tmp = matches[girls[0]]
matches[girls[0]] = matches[girls[1]]
matches[girls[1]] = tmp
print(girls[0] + " and " + girls[1] + " have switched partners")
if checkMatches(guys, girls, matches, guyPrefers, girlPrefers):
    print("Marriages are stable")
else:
    print("Marriages are unstable")