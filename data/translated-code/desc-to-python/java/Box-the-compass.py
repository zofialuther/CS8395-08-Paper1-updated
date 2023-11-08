from enum import Enum

class Compass(Enum):
    N = 0
    NNE = 11.25
    NE = 22.5
    ENE = 33.75
    E = 45
    ESE = 56.25
    SE = 67.5
    SSE = 78.75
    S = 90
    SSW = 101.25
    SW = 112.5
    WSW = 123.75
    W = 135
    WNW = 146.25
    NW = 157.5
    NNW = 168.75

    def midpoint(self):
        next_point = Compass((self.value + 11.25) % 360)
        return next_point

    def bounds(self):
        next_point = Compass((self.value + 11.25) % 360)
        prev_point = Compass((self.value - 11.25) % 360)
        return (prev_point, next_point)

    @classmethod
    def from_degree(cls, degree):
        degree = degree % 360
        for direction in cls:
            if degree <= direction.value:
                return direction
        return cls.N

    def __str__(self):
        return self.name.capitalize()