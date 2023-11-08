from typing import List

def ludicUpTo(n: int) -> List[int]:
    ludics = [i for i in range(1, n+1)]   # fill the initial list
    cursor = 1  # start at index 1 because the first ludic number is 1 and we don't remove anything for it
    while cursor < len(ludics):
        thisLudic = ludics[cursor]  # the first item in the list is a ludic number
        removeCursor = cursor + thisLudic  # start removing that many items later
        while removeCursor < len(ludics):
            ludics.pop(removeCursor)  # remove the next item
            removeCursor = removeCursor + thisLudic - 1  # move the removal cursor up as many spaces as we need to
            # then back one to make up for the item we just removed
    return ludics

def getTriplets(ludics: List[int]) -> List[List[int]]:
    triplets = []
    for i in range(len(ludics) - 2):  # only need to check up to the third to last item
        thisLudic = ludics[i]
        if (thisLudic + 2) in ludics and (thisLudic + 6) in ludics:
            triplet = [thisLudic, thisLudic + 2, thisLudic + 6]
            triplets.append(triplet)
    return triplets

print("First 25 Ludics:", ludicUpTo(110))  # 110 will get us 25 numbers
print("Ludics up to 1000:", len(ludicUpTo(1000)))
print("2000th - 2005th Ludics:", ludicUpTo(22000)[1999:2005])  # 22000 will get us 2005 numbers
print("Triplets up to 250:", getTriplets(ludicUpTo(250)))