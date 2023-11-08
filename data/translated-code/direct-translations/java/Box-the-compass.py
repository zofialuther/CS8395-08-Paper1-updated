from enum import Enum

class Compass(Enum):
    N = 1
    NbE = 2
    NNE = 3
    NEbN = 4
    NE = 5
    NEbE = 6
    ENE = 7
    EbN = 8
    E = 9
    EbS = 10
    ESE = 11
    SEbE = 12
    SE = 13
    SEbS = 14
    SSE = 15
    SbE = 16
    S = 17
    SbW = 18
    SSW = 19
    SWbS = 20
    SW = 21
    SWbW = 22
    WSW = 23
    WbS = 24
    W = 25
    WbN = 26
    WNW = 27
    NWbW = 28
    NW = 29
    NWbN = 30
    NNW = 31
    NbW = 32

    def midpoint(self):
        midpoint = (360 / 32) * self.value
        return 360 if midpoint == 0 else midpoint

    def bounds(self):
        bound = (360 / 32) / 2
        midpoint = self.midpoint()
        boundA = midpoint - bound
        boundB = midpoint + bound
        if boundB > 360:
            boundB -= 360
        return [boundA, boundB]

    @staticmethod
    def parse(degrees):
        boundsN = Compass.N.bounds()
        for value in Compass:
            bounds = value.bounds()
            if degrees >= boundsN[0] or degrees < boundsN[1]:
                return Compass.N
            if degrees >= bounds[0] and degrees < bounds[1]:
                return value
        return None

    def __str__(self):
        strings = ['' for _ in range(len(self.name))]
        index = 0
        for letter in self.name:
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
                string += " {} {}".format(strings[1], strings[2])
            else:
                string += "-{}{}".format(strings[1], strings[2])
        elif len(strings) == 4:
            string += " ".join(strings[1:])
        return string
