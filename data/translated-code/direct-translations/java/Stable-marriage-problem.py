from collections import deque

guys = [
    "abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"
]
girls = [
    "abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"
]
guyPrefers = {
    "abe": ["abi", "eve", "cath", "ivy", "jan", "dee", "fay", "bea", "hope", "gay"],
    "bob": ["cath", "hope", "abi", "dee", "eve", "fay", "bea", "jan", "ivy", "gay"],
    "col": ["hope", "eve", "abi", "dee", "bea", "fay", "ivy", "gay", "cath", "jan"],
    "dan": ["ivy", "fay", "dee", "gay", "hope", "eve", "jan", "bea", "cath", "abi"],
    "ed": ["jan", "dee", "bea", "cath", "fay", "eve", "abi", "ivy", "hope", "gay"],
    "fred": ["bea", "abi", "dee", "gay", "eve", "ivy", "cath", "jan", "hope", "fay"],
    "gav": ["gay", "eve", "ivy", "bea", "cath", "abi", "dee", "hope", "jan", "fay"],
    "hal": ["abi", "eve", "hope", "fay", "ivy", "cath", "jan", "bea", "gay", "dee"],
    "ian": ["hope", "cath", "dee", "gay", "bea", "abi", "fay", "ivy", "jan", "eve"],
    "jon": ["abi", "fay", "jan", "gay", "eve", "bea", "dee", "cath", "ivy", "hope"]
}
girlPrefers = {
    "abi": ["bob", "fred", "jon", "gav", "ian", "abe", "dan", "ed", "col", "hal"],
    "bea": ["bob", "abe", "col", "fred", "gav", "dan", "ian", "ed", "jon", "hal"],
    "cath": ["fred", "bob", "ed", "gav", "hal", "col", "ian", "abe", "dan", "jon"],
    "dee": ["fred", "jon", "col", "abe", "ian", "hal", "gav", "dan", "bob", "ed"],
    "eve": ["jon", "hal", "fred", "dan", "abe", "gav", "col", "ed", "ian", "bob"],
    "fay": ["bob", "abe", "ed", "ian", "jon", "dan", "fred", "gav", "col", "hal"],
    "gay": ["jon", "gav", "hal", "fred", "bob", "abe", "col", "ed", "dan", "ian"],
    "hope": ["gav", "jon", "bob", "abe", "ian", "dan", "hal", "ed", "col", "fred"],
    "ivy": ["ian", "col", "hal", "gav", "fred", "bob", "abe", "ed", "jon", "dan"],
    "jan": ["ed", "hal", "gav", "abe", "bob", "jon", "col", "ian", "fred", "dan"]
}

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
    if set(girls) != set(matches.keys()):
        return False
    if set(guys) != set(matches.values()):
        return False
    invertedMatches = {v: k for k, v in matches.items()}
    for guy, girl in matches.items():
        shePrefers = girlPrefers[girl]
        sheLikesBetter = shePrefers[:shePrefers.index(guy)]
        hePrefers = guyPrefers[guy]
        heLikesBetter = hePrefers[:hePrefers.index(girl)]
        for g in sheLikesBetter:
            guysFiance = invertedMatches[g]
            if guy in guyPrefers[g].index(girlsFiance) > guyPrefers[g].index(guy):
                return False
        for g in heLikesBetter:
            girlsFiance = matches[g]
            if girl in girlPrefers[g].index(guysFiance) > girlPrefers[g].index(girl):
                return False
    return True

matches = match(guys, guyPrefers, girlPrefers)
for guy, girl in matches.items():
    print(guy + " is engaged to " + girl)

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