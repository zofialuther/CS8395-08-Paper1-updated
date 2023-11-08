def pointName(index):
    dirs = [ "N", "NbE", "N-NE", ... ]  # list of compass directions
    charMap = [ ('N', "north"), ('S', "south"), ('E', "east"), ('W', "west"), ('b', " by "), ('-', "-") ]  # mapping of characters to compass direction names
    capitalizedDir = ''.join([charMap[dirs[index].index(char)][1] if char in dirs[index] else '?' for char, _ in charMap]).capitalize()  # capitalize the compass direction
    return capitalizedDir

def pointIndex(degrees):
    index = (round(degrees * 1000) + 5625) % 360000 // 11250  # calculate the compass point index
    return index

def printPointName(degrees):
    deg = float(degrees)  # convert degrees to float
    idx = pointIndex(deg)  # get compass point index
    print(f"{idx + 1} {pointName(idx)} {degrees}")  # print formatted compass point name

def main():
    for i in range(32):  # loop through 32 compass points
        printPointName(i)  # print compass point name