```
compassangle = {
    0: {"name": "N", "abbreviation": "N", "angle": 0},
    1: {"name": "NNE", "abbreviation": "NNE", "angle": 11.25},
    2: {"name": "NE", "abbreviation": "NE", "angle": 22.5},
    3: {"name": "ENE", "abbreviation": "ENE", "angle": 33.75},
    4: {"name": "E", "abbreviation": "E", "angle": 45},
    5: {"name": "ESE", "abbreviation": "ESE", "angle": 56.25},
    6: {"name": "SE", "abbreviation": "SE", "angle": 67.5},
    7: {"name": "SSE", "abbreviation": "SSE", "angle": 78.75},
    8: {"name": "S", "abbreviation": "S", "angle": 90},
    9: {"name": "SSW", "abbreviation": "SSW", "angle": 101.25},
    10: {"name": "SW", "abbreviation": "SW", "angle": 112.5},
    11: {"name": "WSW", "abbreviation": "WSW", "angle": 123.75},
    12: {"name": "W", "abbreviation": "W", "angle": 135},
    13: {"name": "WNW", "abbreviation": "WNW", "angle": 146.25},
    14: {"name": "NW", "abbreviation": "NW", "angle": 157.5},
    15: {"name": "NNW", "abbreviation": "NNW", "angle": 168.75},
    16: {"name": "N", "abbreviation": "N", "angle": 180},
    17: {"name": "NNE", "abbreviation": "NNE", "angle": 191.25},
    18: {"name": "NE", "abbreviation": "NE", "angle": 202.5},
    19: {"name": "ENE", "abbreviation": "ENE", "angle": 213.75},
    20: {"name": "E", "abbreviation": "E", "angle": 225},
    21: {"name": "ESE", "abbreviation": "ESE", "angle": 236.25},
    22: {"name": "SE", "abbreviation": "SE", "angle": 247.5},
    23: {"name": "SSE", "abbreviation": "SSE", "angle": 258.75},
    24: {"name": "S", "abbreviation": "S", "angle": 270},
    25: {"name": "SSW", "abbreviation": "SSW", "angle": 281.25},
    26: {"name": "SW", "abbreviation": "SW", "angle": 292.5},
    27: {"name": "WSW", "abbreviation": "WSW", "angle": 303.75},
    28: {"name": "W", "abbreviation": "W", "angle": 315},
    29: {"name": "WNW", "abbreviation": "WNW", "angle": 326.25},
    30: {"name": "NW", "abbreviation": "NW", "angle": 337.5},
    31: {"name": "NNW", "abbreviation": "NNW", "angle": 348.75}
}

def resolve_index(angle):
    return int(angle / 11.25) % 32

def calculate_angle(index):
    return compassangle[index]["angle"]
```