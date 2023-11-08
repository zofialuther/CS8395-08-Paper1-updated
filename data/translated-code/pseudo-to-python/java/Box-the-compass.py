```python
from enum import Enum

class Compass(Enum):
    N = 0
    NbE = 1
    NNE = 2
    NEbN = 3
    NE = 4
    NEbE = 5
    ENE = 6
    EbN = 7
    E = 8
    EbS = 9
    ESE = 10
    SEbE = 11
    SE = 12
    SEbS = 13
    SSE = 14
    SbE = 15
    S = 16
    SbW = 17
    SSW = 18
    SWbS = 19
    SW = 20
    SWbW = 21
    WSW = 22
    WbS = 23
    W = 24
    WbN = 25
    WNW = 26
    NWbW = 27
    NW = 28
    NWbN = 29
    NNW = 30
    NbW = 31

    def midpoint(self):
        midpoint = (360 / 32) * self.value
        if midpoint == 0:
            return 360
        else:
            return midpoint

    def bounds(self):
        bound = (360 / 32) / 2
        midpoint = self.midpoint()
        boundA = midpoint - bound
        boundB = midpoint + bound
        if boundB > 360:
            boundB -= 360
        return [boundA, boundB]

    def parse(self, degrees):
        boundsN = Compass.N.bounds()
        for value in Compass:
            bounds = value.bounds()
            if degrees >= boundsN[0] or degrees < boundsN[1]:
                return Compass.N
            if degrees >= bounds[0] and degrees < bounds[1]:
                return value
        return None

    def toString(self):
        strings = [c for c in self.name()]
        index = 0
        for letter in self.name():
            if letter == 'N':
                strings[index] = "north"
            elif letter == 'E':
                strings[index] = "east"
            elif letter == 'S':
                strings[index] = "south"
            elif letter == 'W':
                strings[index] = "west"
            elif letter == 'b':
                strings[index] = "by"
            index += 1
        string = strings[0][0].upper() + strings[0][1:]
        if len(strings) == 2:
            string += strings[1]
        elif len(strings) == 3:
            if strings[1] == "by":
                string += " %s %s" % (strings[1], strings[2])
            else:
                string += "-%s%s" % (strings[1], strings[2])
        elif len(strings) == 4:
            string += " ".join([strings[1], strings[2], strings[3]])
        return string
```