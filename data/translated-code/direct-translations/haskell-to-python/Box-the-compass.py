from dataclasses import dataclass
from typing import List
import string

dirs: List[str] = [
    "N",
    "NbE",
    "N-NE",
    "NEbN",
    "NE",
    "NEbE",
    "E-NE",
    "EbN",
    "E",
    "EbS",
    "E-SE",
    "SEbE",
    "SE",
    "SEbS",
    "S-SE",
    "SbE",
    "S",
    "SbW",
    "S-SW",
    "SWbS",
    "SW",
    "SWbW",
    "W-SW",
    "WbS",
    "W",
    "WbN",
    "W-NW",
    "NWbW",
    "NW",
    "NWbN",
    "N-NW",
    "NbW"
]

@dataclass
class Point:
    index: int
    name: str
    degrees: float

def point_name(i: int) -> str:
    def from_char(c: str) -> str:
        return {
            'N': "north",
            'S': "south",
            'E': "east",
            'W': "west",
            'b': " by ",
            '-': "-"
        }.get(c, "?")

    def capitalize(s: str) -> str:
        return s[0].upper() + s[1:]

    return ''.join([from_char(c) for c in dirs[i]]) 

def point_index(deg: float) -> int:
    return (round(deg * 1000) + 5625) % 360000 // 11250

def print_point_name(deg: str) -> None:
    deg = float(deg)
    idx = point_index(deg)
    name = point_name(idx)
    print(f"{idx + 1:2d}  {name:18s}  {deg:6.2f}°")

def main() -> None:
    for i in range(32):
        print_point_name(str(i))

main()